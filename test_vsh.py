import unittest
import vsh
import numpy as np


class FEKOCompare(unittest.TestCase):
    """
    Testing the output to the some FEKO outputs
    """
    def test_TE_0_1(self):
        vsh_theta, vsh_phi = vsh.vsh(0, 0, 1, 0, 0)
        self.assertEqual(np.abs(vsh_theta), 0)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 0, 3)

        vsh_theta, vsh_phi = vsh.vsh(0, 0, 1, np.pi/4, 0)
        self.assertAlmostEqual(np.abs(np.angle(vsh_phi[0])), np.pi, 3)
        self.assertEqual(np.abs(vsh_theta), 0)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 4.742, 3)

        vsh_theta, vsh_phi = vsh.vsh(0, 0, 1, np.pi/2, np.pi/4)
        self.assertAlmostEqual(np.abs(np.angle(vsh_phi[0])), np.pi, 3)
        self.assertEqual(np.abs(vsh_theta), 0)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 6.706, 3)

    def test_TM_0_1(self):
        vsh_theta, vsh_phi = vsh.vsh(1, 0, 1, 0, 0)
        self.assertEqual(np.angle(vsh_phi), 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 0, 3)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 0, 3)

        vsh_theta, vsh_phi = vsh.vsh(1, 0, 1, np.pi/4, 0)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), -np.pi/2, 3)
        self.assertEqual(np.abs(vsh_phi), 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 4.742, 3)

        vsh_theta, vsh_phi = vsh.vsh(1, 0, 1, np.pi/2, np.pi/4)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), -np.pi/2, 3)
        self.assertEqual(np.abs(vsh_phi), 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 6.706, 3)

    def test_TE_1_1(self):
        vsh_theta, vsh_phi = vsh.vsh(0, 1, 1, 0, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 4.742, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 4.742, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), -np.pi/2, 3)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), 0, 3)

        vsh_theta, vsh_phi = vsh.vsh(0, 1, 1, np.pi / 4, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 4.742, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 3.354, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), -np.pi/2, 3)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), 0, 3)

        vsh_theta, vsh_phi = vsh.vsh(0, 1, 1, np.pi / 2, np.pi / 4)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 4.742, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 0, 2)

    def test_TM_1_1(self):
        vsh_theta, vsh_phi = vsh.vsh(1, 1, 1, 0, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 4.742, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 4.742, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), np.pi/2, 3)
        self.assertAlmostEqual(np.abs(np.angle(vsh_phi[0])), np.pi, 3)

        vsh_theta, vsh_phi = vsh.vsh(1, 1, 1, np.pi / 4, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 3.354, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 4.742, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), np.pi/2, 3)
        self.assertAlmostEqual(np.abs(np.angle(vsh_phi[0])), np.pi, 3)

        vsh_theta, vsh_phi = vsh.vsh(1, 1, 1, np.pi / 2, np.pi / 4)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 0, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 4.742, 2)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), -(np.pi/2 + np.pi/4), 3)

    def test_TE_n1_1(self):
        vsh_theta, vsh_phi = vsh.vsh(0, -1, 1, 0, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 4.742, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 4.742, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), -np.pi/2, 3)
        self.assertAlmostEqual(np.abs(np.angle(vsh_phi[0])), np.pi, 3)

        vsh_theta, vsh_phi = vsh.vsh(0, -1, 1, np.pi/2+np.pi/4, 0)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), -np.pi / 2, 3)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), 0, 3)

        vsh_theta, vsh_phi = vsh.vsh(0, -1, 1, np.pi / 4, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 4.742, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 3.354, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), -np.pi/2, 3)
        self.assertAlmostEqual(np.abs(np.angle(vsh_phi[0])), np.pi, 3)

        vsh_theta, vsh_phi = vsh.vsh(0, -1, 1, np.pi / 2, np.pi / 4)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 4.742, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 0, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), -(np.pi/2 + np.pi/4), 3)

    def test_TM_n1_1(self):
        vsh_theta, vsh_phi = vsh.vsh(1, -1, 1, 0, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 4.742, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 4.742, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), -np.pi/2, 3)
        self.assertAlmostEqual(np.abs(np.angle(vsh_phi[0])), np.pi, 3)

        vsh_theta, vsh_phi = vsh.vsh(1, -1, 1, np.pi / 4, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 3.354, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 4.742, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), -np.pi/2, 3)
        self.assertAlmostEqual(np.abs(np.angle(vsh_phi[0])), np.pi, 3)

        vsh_theta, vsh_phi = vsh.vsh(1, -1, 1, np.pi / 2, np.pi / 4)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 0, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 4.742, 2)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), (np.pi/2 + np.pi/4), 3)

    def test_TE_0_2(self):
        vsh_theta, vsh_phi = vsh.vsh(0, 0, 2, 0, 0)
        self.assertEqual(np.abs(vsh_theta), 0)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 0, 3)

        vsh_theta, vsh_phi = vsh.vsh(0, 0, 2, np.pi/4, 0)
        self.assertEqual(np.abs(vsh_theta), 0)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 7.497, 2)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), -np.pi/2, 3)

        vsh_theta, vsh_phi = vsh.vsh(0, 0, 2, np.pi/2, np.pi/4)
        self.assertEqual(np.abs(vsh_theta), 0)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 0, 2)

    def test_TM_0_2(self):
        vsh_theta, vsh_phi = vsh.vsh(1, 0, 2, 0, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 0, 3)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 0, 3)

        vsh_theta, vsh_phi = vsh.vsh(1, 0, 2, np.pi/4, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 7.497, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 0, 2)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), 0, 3)

        vsh_theta, vsh_phi = vsh.vsh(1, 0, 2, np.pi/2, np.pi/4)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 0, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 0, 2)

    def test_TE_1_2(self):
        vsh_theta, vsh_phi = vsh.vsh(0, 1, 2, 0, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 6.121, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 6.121, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), 0, 3)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), np.pi/2, 3)

        vsh_theta, vsh_phi = vsh.vsh(0, 1, 2, np.pi / 4, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 4.328, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 0, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), 0, 3)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), -np.pi/2, 3)

        vsh_theta, vsh_phi = vsh.vsh(0, 1, 2, np.pi / 2, np.pi / 4)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 0, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 6.121, 2)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), -np.pi/4, 3)

    def test_TM_n1_3(self):
        vsh_theta, vsh_phi = vsh.vsh(1, -1, 3, 0, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 7.245, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 7.245, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), np.pi/2, 3)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), 0, 3)

        vsh_theta, vsh_phi = vsh.vsh(1, -1, 3, np.pi / 4, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 4.482, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 2.716, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), -np.pi/2, 3)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), 0, 3)

        vsh_theta, vsh_phi = vsh.vsh(1, -1, 3, np.pi / 2, np.pi / 4)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 0, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 1.809, 2)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), np.pi/2 + np.pi/4, 3)

    def test_TE_2_2(self):
        vsh_theta, vsh_phi = vsh.vsh(0, 2, 2, 0, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 0, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 0, 2)

        vsh_theta, vsh_phi = vsh.vsh(0, 2, 2, np.pi / 4, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 4.329, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 3.061, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), 0, 3)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), np.pi/2, 3)

        vsh_theta, vsh_phi = vsh.vsh(0, 2, 2, np.pi / 2, np.pi / 4)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 6.121, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 0, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), np.pi/2, 3)

    def test_TM_n1_3(self):
        vsh_theta, vsh_phi = vsh.vsh(1, -1, 3, 0, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 7.246, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 7.241, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), np.pi/2, 3)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), 0, 3)

        vsh_theta, vsh_phi = vsh.vsh(1, -1, 3, np.pi / 4, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 4.482, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 2.716, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), -np.pi/2, 3)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), 0, 3)

        vsh_theta, vsh_phi = vsh.vsh(1, -1, 3, np.pi / 2, np.pi / 4)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 0, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 1.811, 2)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), np.pi/2+np.pi/4, 3)

    def test_TE_n1_3(self):
        vsh_theta, vsh_phi = vsh.vsh(0, -1, 3, 0, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 7.243, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 7.243, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), np.pi / 2, 3)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), 0, 3)

        vsh_theta, vsh_phi = vsh.vsh(0, -1, 3, np.pi / 4, 0)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 2.716, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 4.482, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), np.pi / 2, 3)
        self.assertAlmostEqual(np.angle(vsh_phi[0]), np.pi, 3)

        vsh_theta, vsh_phi = vsh.vsh(0, -1, 3, np.pi / 2, np.pi / 4)
        self.assertAlmostEqual(np.abs(vsh_theta[0]), 1.811, 2)
        self.assertAlmostEqual(np.abs(vsh_phi[0]), 0, 2)
        self.assertAlmostEqual(np.angle(vsh_theta[0]), -np.pi / 2 - np.pi / 4, 3)


class j2smn(unittest.TestCase):
    def test_s(self):
        s, m, n = vsh.j2smn(1)
        self.assertEqual(s, 1)
        s, m, n = vsh.j2smn(2)
        self.assertEqual(s, 2)
        s, m, n = vsh.j2smn(22)
        self.assertEqual(s, 2)

    def test_n(self):
        s, m, n = vsh.j2smn(1)
        self.assertEqual(n, 1)
        s, m, n = vsh.j2smn(2)
        self.assertEqual(n, 1)
        s, m, n = vsh.j2smn(22)
        self.assertEqual(n, 3)

    def test_m(self):
        s, m, n = vsh.j2smn(1)
        self.assertEqual(m, -1)
        s, m, n = vsh.j2smn(2)
        self.assertEqual(m, -1)
        s, m, n = vsh.j2smn(28)
        self.assertEqual(m, 2)

    def test_gen(self):
        s, m, n = vsh.j2smn(213)
        self.assertEqual(s, 1)
        self.assertEqual(m, -3)
        self.assertEqual(n, 10)



if __name__ == '__main__':
    unittest.main()
