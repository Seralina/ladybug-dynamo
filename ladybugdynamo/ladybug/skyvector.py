
class Skyvectors(object):
    """vector for sky patches

        Attributes:
            skyDensity: Density of the sky. 0 generates a Tregenza sky, which will
                divide up the sky dome with a coarse density of 145 sky patches.
                Set to 1 to generate a Reinhart sky, which will divide up the sky dome
                using a density of 580 sky patches.

            patchNumber: Number of sky patch. 0-144 for Tregenza sky, 0-579 for Reinhart sky

        Return:
            Return a tuple with 3 values that represents the sky vector as x, y, z if patchNumber is provided
            otherwise it returns all the vectors as a list of (x, y, z) values. Vectors are looking outwards
            from the center of the sky
    """

    def __init__(self, skyDensity=0):
        """Init class."""
        __numberOfPatches = {0 :146, 1: 578}
        assert -1 < int(skyDensity) <= 1, "Sky density is should be 0: Tregenza sky, 1: Reinhart sky"
        self.__skyDensity = int(skyDensity)
        self.__loadVectors()

    def getVector(self, patchNumber):
        """Get vector for sky patch."""
        if not patchNumber:
            # return all the vectors
            return self.__vectors[self.__skyDensity]

        assert -1 < int(patchNumber) <= self.__numberOfPatches[self.__skyDensity], \
            "Number of sky patch should be between 0 to %d." % \
                self.__numberOfPatches[self.__skyDensity]

        return self.__vectors[self.__skyDensity][int(patchNumber)]

    def __loadVectors(self):

        self.__vectors = {0: (
            (0.0, 0.0, -1),
            (0.0, 0.994522, 0.104528), (0.206773, 0.972789, 0.104528), (0.404508, 0.908541, 0.104528),
            (0.584565, 0.804585, 0.104528), (0.739074, 0.665465, 0.104528), (0.861281, 0.497261, 0.104528),
            (0.945847, 0.307324, 0.104528), (0.989074, 0.103956, 0.104528), (0.989074, 0.103956, 0.104528),
            (0.945847, 0.307324, 0.104528), (0.861281, 0.497261, 0.104528), (0.739074, 0.665465, 0.104528),
            (0.584565, 0.804585, 0.104528), (0.404508, 0.908541, 0.104528), (0.206773, 0.972789, 0.104528),
            (0.0, 0.994522, 0.104528), (-0.206773, 0.972789, 0.104528), (-0.404508, 0.908541, 0.104528),
            (-0.584565, 0.804585, 0.104528), (-0.739074, 0.665465, 0.104528), (-0.861281, 0.497261, 0.104528),
            (-0.945847, 0.307324, 0.104528), (-0.989074, 0.103956, 0.104528), (-0.989074, 0.103956, 0.104528),
            (-0.945847, 0.307324, 0.104528), (-0.861281, 0.497261, 0.104528), (-0.739074, 0.665465, 0.104528),
            (-0.584565, 0.804585, 0.104528), (-0.404508, 0.908541, 0.104528), (-0.206773, 0.972789, 0.104528),
            (0.0, 0.951057, 0.309017), (0.197736, 0.930274, 0.309017), (0.38683, 0.868833, 0.309017),
            (0.559017, 0.769421, 0.309017), (0.706773, 0.636381, 0.309017), (0.823639, 0.475528, 0.309017),
            (0.904508, 0.293893, 0.309017), (0.945847, 0.099412, 0.309017), (0.945847, 0.099412, 0.309017),
            (0.904508, 0.293893, 0.309017), (0.823639, 0.475528, 0.309017), (0.706773, 0.636381, 0.309017),
            (0.559017, 0.769421, 0.309017), (0.38683, 0.868833, 0.309017), (0.197736, 0.930274, 0.309017),
            (0.0, 0.951057, 0.309017), (-0.197736, 0.930274, 0.309017), (-0.38683, 0.868833, 0.309017),
            (-0.559017, 0.769421, 0.309017), (-0.706773, 0.636381, 0.309017), (-0.823639, 0.475528, 0.309017),
            (-0.904508, 0.293893, 0.309017), (-0.945847, 0.099412, 0.309017), (-0.945847, 0.099412, 0.309017),
            (-0.904508, 0.293893, 0.309017), (-0.823639, 0.475528, 0.309017), (-0.706773, 0.636381, 0.309017),
            (-0.559017, 0.769421, 0.309017), (-0.38683, 0.868833, 0.309017), (-0.197736, 0.930274, 0.309017),
            (0.0, 0.866025, 0.5), (0.224144, 0.836516, 0.5), (0.433013, 0.75, 0.5), (0.612372, 0.612372, 0.5),
            (0.75, 0.433013, 0.5), (0.836516, 0.224144, 0.5), (0.866025, 0.0, 0.5), (0.836516, 0.224144, 0.5),
            (0.75, 0.433013, 0.5), (0.612372, 0.612372, 0.5), (0.433013, 0.75, 0.5), (0.224144, 0.836516, 0.5),
            (0.0, 0.866025, 0.5), (-0.224144, 0.836516, 0.5), (-0.433013, 0.75, 0.5), (-0.612372, 0.612372, 0.5),
            (-0.75, 0.433013, 0.5), (-0.836516, 0.224144, 0.5), (-0.866025, 0.0, 0.5), (-0.836516, 0.224144, 0.5),
            (-0.75, 0.433013, 0.5), (-0.612372, 0.612372, 0.5), (-0.433013, 0.75, 0.5), (-0.224144, 0.836516, 0.5),
            (0.0, 0.743145, 0.669131), (0.19234, 0.717823, 0.669131), (0.371572, 0.643582, 0.669131), (0.525483, 0.525483, 0.669131),
            (0.643582, 0.371572, 0.669131), (0.717823, 0.19234, 0.669131), (0.743145, 0.0, 0.669131), (0.717823, 0.19234, 0.669131),
            (0.643582, 0.371572, 0.669131), (0.525483, 0.525483, 0.669131), (0.371572, 0.643582, 0.669131),
            (0.19234, 0.717823, 0.669131), (0.0, 0.743145, 0.669131), (-0.19234, 0.717823, 0.669131),
            (-0.371572, 0.643582, 0.669131), (-0.525483, 0.525483, 0.669131), (-0.643582, 0.371572, 0.669131),
            (-0.717823, 0.19234, 0.669131), (-0.743145, 0.0, 0.669131), (-0.717823, 0.19234, 0.669131),
            (-0.643582, 0.371572, 0.669131), (-0.525483, 0.525483, 0.669131), (-0.371572, 0.643582, 0.669131),
            (-0.19234, 0.717823, 0.669131), (0.0, 0.587785, 0.809017), (0.201034, 0.552337, 0.809017),
            (0.377821, 0.45027, 0.809017), (0.509037, 0.293893, 0.809017), (0.578855, 0.102068, 0.809017),
            (0.578855, 0.102068, 0.809017), (0.509037, 0.293893, 0.809017), (0.377821, 0.45027, 0.809017),
            (0.201034, 0.552337, 0.809017), (0.0, 0.587785, 0.809017), (-0.201034, 0.552337, 0.809017),
            (-0.377821, 0.45027, 0.809017), (-0.509037, 0.293893, 0.809017), (-0.578855, 0.102068, 0.809017),
            (-0.578855, 0.102068, 0.809017), (-0.509037, 0.293893, 0.809017), (-0.377821, 0.45027, 0.809017),
            (-0.201034, 0.552337, 0.809017), (0.0, 0.406737, 0.913545), (0.203368, 0.352244, 0.913545),
            (0.352244, 0.203368, 0.913545), (0.406737, 0.0, 0.913545), (0.352244, 0.203368, 0.913545),
            (0.203368, 0.352244, 0.913545), (0.0, 0.406737, 0.913545), (-0.203368, 0.352244, 0.913545),
            (-0.352244, 0.203368, 0.913545), (-0.406737, 0.0, 0.913545), (-0.352244, 0.203368, 0.913545),
            (-0.203368, 0.352244, 0.913545), (0.0, 0.207912, 0.978148), (0.180057, 0.103956, 0.978148),
            (0.180057, 0.103956, 0.978148), (0.0, 0.207912, 0.978148), (-0.180057, 0.103956, 0.978148),
            (-0.180057, 0.103956, 0.978148), (0.0, 0.0, 1)
        ),

            1: (
            (0.0, 0.0, 1),
            (0.0, 0.998533, 0.054139), (0.104375, 0.993063, 0.054139), (0.207607, 0.976713, 0.054139),
            (0.308564, 0.949662, 0.054139), (0.40614, 0.912206, 0.054139), (0.499267, 0.864755, 0.054139),
            (0.586923, 0.807831, 0.054139), (0.668149, 0.742055, 0.054139), (0.742055, 0.668149, 0.054139),
            (0.807831, 0.586923, 0.054139), (0.864755, 0.499267, 0.054139), (0.912206, 0.40614, 0.054139),
            (0.949662, 0.308564, 0.054139), (0.976713, 0.207607, 0.054139), (0.993063, 0.104375, 0.054139),
            (0.998533, 0.0, 0.054139), (0.993063, 0.104375, 0.054139), (0.976713, 0.207607, 0.054139),
            (0.949662, 0.308564, 0.054139), (0.912206, 0.40614, 0.054139), (0.864755, 0.499267, 0.054139),
            (0.807831, 0.586923, 0.054139), (0.742055, 0.668149, 0.054139), (0.668149, 0.742055, 0.054139),
            (0.586923, 0.807831, 0.054139), (0.499267, 0.864755, 0.054139), (0.40614, 0.912206, 0.054139),
            (0.308564, 0.949662, 0.054139), (0.207607, 0.976713, 0.054139), (0.104375, 0.993063, 0.054139),
            (0.0, 0.998533, 0.054139), (-0.104375, 0.993063, 0.054139), (-0.207607, 0.976713, 0.054139),
            (-0.308564, 0.949662, 0.054139), (-0.40614, 0.912206, 0.054139), (-0.499267, 0.864755, 0.054139),
            (-0.586923, 0.807831, 0.054139), (-0.668149, 0.742055, 0.054139), (-0.742055, 0.668149, 0.054139),
            (-0.807831, 0.586923, 0.054139), (-0.864755, 0.499267, 0.054139), (-0.912206, 0.40614, 0.054139),
            (-0.949662, 0.308564, 0.054139), (-0.976713, 0.207607, 0.054139), (-0.993063, 0.104375, 0.054139),
            (-0.998533, 0.0, 0.054139), (-0.993063, 0.104375, 0.054139), (-0.976713, 0.207607, 0.054139),
            (-0.949662, 0.308564, 0.054139), (-0.912206, 0.40614, 0.054139), (-0.864755, 0.499267, 0.054139),
            (-0.807831, 0.586923, 0.054139), (-0.742055, 0.668149, 0.054139), (-0.668149, 0.742055, 0.054139),
            (-0.586923, 0.807831, 0.054139), (-0.499267, 0.864755, 0.054139), (-0.40614, 0.912206, 0.054139),
            (-0.308564, 0.949662, 0.054139), (-0.207607, 0.976713, 0.054139), (-0.104375, 0.993063, 0.054139),
            (0.0, 0.986827, 0.161782), (0.103151, 0.981421, 0.161782), (0.205173, 0.965262, 0.161782),
            (0.304946, 0.938528, 0.161782), (0.401379, 0.901511, 0.161782), (0.493413, 0.854617, 0.161782),
            (0.580042, 0.798359, 0.161782), (0.660316, 0.733355, 0.161782), (0.733355, 0.660316, 0.161782),
            (0.798359, 0.580042, 0.161782), (0.854617, 0.493413, 0.161782), (0.901511, 0.401379, 0.161782),
            (0.938528, 0.304946, 0.161782), (0.965262, 0.205173, 0.161782), (0.981421, 0.103151, 0.161782),
            (0.986827, 0.0, 0.161782), (0.981421, 0.103151, 0.161782), (0.965262, 0.205173, 0.161782),
            (0.938528, 0.304946, 0.161782), (0.901511, 0.401379, 0.161782), (0.854617, 0.493413, 0.161782),
            (0.798359, 0.580042, 0.161782), (0.733355, 0.660316, 0.161782), (0.660316, 0.733355, 0.161782),
            (0.580042, 0.798359, 0.161782), (0.493413, 0.854617, 0.161782), (0.401379, 0.901511, 0.161782),
            (0.304946, 0.938528, 0.161782), (0.205173, 0.965262, 0.161782), (0.103151, 0.981421, 0.161782),
            (0.0, 0.986827, 0.161782), (-0.103151, 0.981421, 0.161782), (-0.205173, 0.965262, 0.161782),
            (-0.304946, 0.938528, 0.161782), (-0.401379, 0.901511, 0.161782), (-0.493413, 0.854617, 0.161782),
            (-0.580042, 0.798359, 0.161782), (-0.660316, 0.733355, 0.161782), (-0.733355, 0.660316, 0.161782),
            (-0.798359, 0.580042, 0.161782), (-0.854617, 0.493413, 0.161782), (-0.901511, 0.401379, 0.161782),
            (-0.938528, 0.304946, 0.161782), (-0.965262, 0.205173, 0.161782), (-0.981421, 0.103151, 0.161782),
            (-0.986827, 0.0, 0.161782), (-0.981421, 0.103151, 0.161782), (-0.965262, 0.205173, 0.161782),
            (-0.938528, 0.304946, 0.161782), (-0.901511, 0.401379, 0.161782), (-0.854617, 0.493413, 0.161782),
            (-0.798359, 0.580042, 0.161782), (-0.733355, 0.660316, 0.161782), (-0.660316, 0.733355, 0.161782),
            (-0.580042, 0.798359, 0.161782), (-0.493413, 0.854617, 0.161782), (-0.401379, 0.901511, 0.161782),
            (-0.304946, 0.938528, 0.161782), (-0.205173, 0.965262, 0.161782), (-0.103151, 0.981421, 0.161782),
            (0.0, 0.96355, 0.267528), (0.100718, 0.958272, 0.267528), (0.200333, 0.942494, 0.267528),
            (0.297753, 0.91639, 0.267528), (0.391911, 0.880247, 0.267528), (0.481775, 0.834459, 0.267528),
            (0.56636, 0.779528, 0.267528), (0.644741, 0.716057, 0.267528), (0.716057, 0.644741, 0.267528),
            (0.779528, 0.56636, 0.267528), (0.834459, 0.481775, 0.267528), (0.880247, 0.391911, 0.267528),
            (0.91639, 0.297753, 0.267528), (0.942494, 0.200333, 0.267528), (0.958272, 0.100718, 0.267528),
            (0.96355, 0.0, 0.267528), (0.958272, 0.100718, 0.267528), (0.942494, 0.200333, 0.267528),
            (0.91639, 0.297753, 0.267528), (0.880247, 0.391911, 0.267528), (0.834459, 0.481775, 0.267528),
            (0.779528, 0.56636, 0.267528), (0.716057, 0.644741, 0.267528), (0.644741, 0.716057, 0.267528),
            (0.56636, 0.779528, 0.267528), (0.481775, 0.834459, 0.267528), (0.391911, 0.880247, 0.267528),
            (0.297753, 0.91639, 0.267528), (0.200333, 0.942494, 0.267528), (0.100718, 0.958272, 0.267528),
            (0.0, 0.96355, 0.267528), (-0.100718, 0.958272, 0.267528), (-0.200333, 0.942494, 0.267528),
            (-0.297753, 0.91639, 0.267528), (-0.391911, 0.880247, 0.267528), (-0.481775, 0.834459, 0.267528),
            (-0.56636, 0.779528, 0.267528), (-0.644741, 0.716057, 0.267528), (-0.716057, 0.644741, 0.267528),
            (-0.779528, 0.56636, 0.267528), (-0.834459, 0.481775, 0.267528), (-0.880247, 0.391911, 0.267528),
            (-0.91639, 0.297753, 0.267528), (-0.942494, 0.200333, 0.267528), (-0.958272, 0.100718, 0.267528),
            (-0.96355, 0.0, 0.267528), (-0.958272, 0.100718, 0.267528), (-0.942494, 0.200333, 0.267528),
            (-0.91639, 0.297753, 0.267528), (-0.880247, 0.391911, 0.267528), (-0.834459, 0.481775, 0.267528),
            (-0.779528, 0.56636, 0.267528), (-0.716057, 0.644741, 0.267528), (-0.644741, 0.716057, 0.267528),
            (-0.56636, 0.779528, 0.267528), (-0.481775, 0.834459, 0.267528), (-0.391911, 0.880247, 0.267528),
            (-0.297753, 0.91639, 0.267528), (-0.200333, 0.942494, 0.267528), (-0.100718, 0.958272, 0.267528),
            (0.0, 0.928977, 0.370138), (0.097105, 0.923888, 0.370138), (0.193145, 0.908676, 0.370138),
            (0.28707, 0.883509, 0.370138), (0.377849, 0.848662, 0.370138), (0.464488, 0.804517, 0.370138),
            (0.546039, 0.751558, 0.370138), (0.621607, 0.690364, 0.370138), (0.690364, 0.621607, 0.370138),
            (0.751558, 0.546039, 0.370138), (0.804517, 0.464488, 0.370138), (0.848662, 0.377849, 0.370138),
            (0.883509, 0.28707, 0.370138), (0.908676, 0.193145, 0.370138), (0.923888, 0.097105, 0.370138),
            (0.928977, 0.0, 0.370138), (0.923888, 0.097105, 0.370138), (0.908676, 0.193145, 0.370138),
            (0.883509, 0.28707, 0.370138), (0.848662, 0.377849, 0.370138), (0.804517, 0.464488, 0.370138),
            (0.751558, 0.546039, 0.370138), (0.690364, 0.621607, 0.370138), (0.621607, 0.690364, 0.370138),
            (0.546039, 0.751558, 0.370138), (0.464488, 0.804517, 0.370138), (0.377849, 0.848662, 0.370138),
            (0.28707, 0.883509, 0.370138), (0.193145, 0.908676, 0.370138), (0.097105, 0.923888, 0.370138),
            (0.0, 0.928977, 0.370138), (-0.097105, 0.923888, 0.370138), (-0.193145, 0.908676, 0.370138),
            (-0.28707, 0.883509, 0.370138), (-0.377849, 0.848662, 0.370138), (-0.464488, 0.804517, 0.370138),
            (-0.546039, 0.751558, 0.370138), (-0.621607, 0.690364, 0.370138), (-0.690364, 0.621607, 0.370138),
            (-0.751558, 0.546039, 0.370138), (-0.804517, 0.464488, 0.370138), (-0.848662, 0.377849, 0.370138),
            (-0.883509, 0.28707, 0.370138), (-0.908676, 0.193145, 0.370138), (-0.923888, 0.097105, 0.370138),
            (-0.928977, 0.0, 0.370138), (-0.923888, 0.097105, 0.370138), (-0.908676, 0.193145, 0.370138),
            (-0.883509, 0.28707, 0.370138), (-0.848662, 0.377849, 0.370138), (-0.804517, 0.464488, 0.370138),
            (-0.751558, 0.546039, 0.370138), (-0.690364, 0.621607, 0.370138), (-0.621607, 0.690364, 0.370138),
            (-0.546039, 0.751558, 0.370138), (-0.464488, 0.804517, 0.370138), (-0.377849, 0.848662, 0.370138),
            (-0.28707, 0.883509, 0.370138), (-0.193145, 0.908676, 0.370138), (-0.097105, 0.923888, 0.370138),
            (0.0, 0.883512, 0.468408), (0.115321, 0.875953, 0.468408), (0.22867, 0.853407, 0.468408),
            (0.338105, 0.816259, 0.468408), (0.441756, 0.765144, 0.468408), (0.537848, 0.700937, 0.468408),
            (0.624737, 0.624737, 0.468408), (0.700937, 0.537848, 0.468408), (0.765144, 0.441756, 0.468408),
            (0.816259, 0.338105, 0.468408), (0.853407, 0.22867, 0.468408), (0.875953, 0.115321, 0.468408),
            (0.883512, 0.0, 0.468408), (0.875953, 0.115321, 0.468408), (0.853407, 0.22867, 0.468408),
            (0.816259, 0.338105, 0.468408), (0.765144, 0.441756, 0.468408), (0.700937, 0.537848, 0.468408),
            (0.624737, 0.624737, 0.468408), (0.537848, 0.700937, 0.468408), (0.441756, 0.765144, 0.468408),
            (0.338105, 0.816259, 0.468408), (0.22867, 0.853407, 0.468408), (0.115321, 0.875953, 0.468408),
            (0.0, 0.883512, 0.468408), (-0.115321, 0.875953, 0.468408), (-0.22867, 0.853407, 0.468408),
            (-0.338105, 0.816259, 0.468408), (-0.441756, 0.765144, 0.468408), (-0.537848, 0.700937, 0.468408),
            (-0.624737, 0.624737, 0.468408), (-0.700937, 0.537848, 0.468408), (-0.765144, 0.441756, 0.468408),
            (-0.816259, 0.338105, 0.468408), (-0.853407, 0.22867, 0.468408), (-0.875953, 0.115321, 0.468408),
            (-0.883512, 0.0, 0.468408), (-0.875953, 0.115321, 0.468408), (-0.853407, 0.22867, 0.468408),
            (-0.816259, 0.338105, 0.468408), (-0.765144, 0.441756, 0.468408), (-0.700937, 0.537848, 0.468408),
            (-0.624737, 0.624737, 0.468408), (-0.537848, 0.700937, 0.468408), (-0.441756, 0.765144, 0.468408),
            (-0.338105, 0.816259, 0.468408), (-0.22867, 0.853407, 0.468408), (-0.115321, 0.875953, 0.468408),
            (0.0, 0.827689, 0.561187), (0.108035, 0.820608, 0.561187), (0.214222, 0.799486, 0.561187),
            (0.316743, 0.764685, 0.561187), (0.413844, 0.7168, 0.561187), (0.503865, 0.65665, 0.561187),
            (0.585265, 0.585265, 0.561187), (0.65665, 0.503865, 0.561187), (0.7168, 0.413844, 0.561187),
            (0.764685, 0.316743, 0.561187), (0.799486, 0.214222, 0.561187), (0.820608, 0.108035, 0.561187),
            (0.827689, 0.0, 0.561187), (0.820608, 0.108035, 0.561187), (0.799486, 0.214222, 0.561187),
            (0.764685, 0.316743, 0.561187), (0.7168, 0.413844, 0.561187), (0.65665, 0.503865, 0.561187),
            (0.585265, 0.585265, 0.561187), (0.503865, 0.65665, 0.561187), (0.413844, 0.7168, 0.561187),
            (0.316743, 0.764685, 0.561187), (0.214222, 0.799486, 0.561187), (0.108035, 0.820608, 0.561187),
            (0.0, 0.827689, 0.561187), (-0.108035, 0.820608, 0.561187), (-0.214222, 0.799486, 0.561187),
            (-0.316743, 0.764685, 0.561187), (-0.413844, 0.7168, 0.561187), (-0.503865, 0.65665, 0.561187),
            (-0.585265, 0.585265, 0.561187), (-0.65665, 0.503865, 0.561187), (-0.7168, 0.413844, 0.561187),
            (-0.764685, 0.316743, 0.561187), (-0.799486, 0.214222, 0.561187), (-0.820608, 0.108035, 0.561187),
            (-0.827689, 0.0, 0.561187), (-0.820608, 0.108035, 0.561187), (-0.799486, 0.214222, 0.561187),
            (-0.764685, 0.316743, 0.561187), (-0.7168, 0.413844, 0.561187), (-0.65665, 0.503865, 0.561187),
            (-0.585265, 0.585265, 0.561187), (-0.503865, 0.65665, 0.561187), (-0.413844, 0.7168, 0.561187),
            (-0.316743, 0.764685, 0.561187), (-0.214222, 0.799486, 0.561187), (-0.108035, 0.820608, 0.561187),
            (0.0, 0.762162, 0.647386), (0.099482, 0.755642, 0.647386), (0.197262, 0.736192, 0.647386),
            (0.291667, 0.704146, 0.647386), (0.381081, 0.660052, 0.647386), (0.463975, 0.604664, 0.647386),
            (0.53893, 0.53893, 0.647386), (0.604664, 0.463975, 0.647386), (0.660052, 0.381081, 0.647386),
            (0.704146, 0.291667, 0.647386), (0.736192, 0.197262, 0.647386), (0.755642, 0.099482, 0.647386),
            (0.762162, 0.0, 0.647386), (0.755642, 0.099482, 0.647386), (0.736192, 0.197262, 0.647386),
            (0.704146, 0.291667, 0.647386), (0.660052, 0.381081, 0.647386), (0.604664, 0.463975, 0.647386),
            (0.53893, 0.53893, 0.647386), (0.463975, 0.604664, 0.647386), (0.381081, 0.660052, 0.647386),
            (0.291667, 0.704146, 0.647386), (0.197262, 0.736192, 0.647386), (0.099482, 0.755642, 0.647386),
            (0.0, 0.762162, 0.647386), (-0.099482, 0.755642, 0.647386), (-0.197262, 0.736192, 0.647386),
            (-0.291667, 0.704146, 0.647386), (-0.381081, 0.660052, 0.647386), (-0.463975, 0.604664, 0.647386),
            (-0.53893, 0.53893, 0.647386), (-0.604664, 0.463975, 0.647386), (-0.660052, 0.381081, 0.647386),
            (-0.704146, 0.291667, 0.647386), (-0.736192, 0.197262, 0.647386), (-0.755642, 0.099482, 0.647386),
            (-0.762162, 0.0, 0.647386), (-0.755642, 0.099482, 0.647386), (-0.736192, 0.197262, 0.647386),
            (-0.704146, 0.291667, 0.647386), (-0.660052, 0.381081, 0.647386), (-0.604664, 0.463975, 0.647386),
            (-0.53893, 0.53893, 0.647386), (-0.463975, 0.604664, 0.647386), (-0.381081, 0.660052, 0.647386),
            (-0.291667, 0.704146, 0.647386), (-0.197262, 0.736192, 0.647386), (-0.099482, 0.755642, 0.647386),
            (0.0, 0.687699, 0.725995), (0.089763, 0.681816, 0.725995), (0.17799, 0.664267, 0.725995),
            (0.263171, 0.635351, 0.725995), (0.34385, 0.595565, 0.725995), (0.418645, 0.545589, 0.725995),
            (0.486277, 0.486277, 0.725995), (0.545589, 0.418645, 0.725995), (0.595565, 0.34385, 0.725995),
            (0.635351, 0.263171, 0.725995), (0.664267, 0.17799, 0.725995), (0.681816, 0.089763, 0.725995),
            (0.687699, 0.0, 0.725995), (0.681816, 0.089763, 0.725995), (0.664267, 0.17799, 0.725995),
            (0.635351, 0.263171, 0.725995), (0.595565, 0.34385, 0.725995), (0.545589, 0.418645, 0.725995),
            (0.486277, 0.486277, 0.725995), (0.418645, 0.545589, 0.725995), (0.34385, 0.595565, 0.725995),
            (0.263171, 0.635351, 0.725995), (0.17799, 0.664267, 0.725995), (0.089763, 0.681816, 0.725995),
            (0.0, 0.687699, 0.725995), (-0.089763, 0.681816, 0.725995), (-0.17799, 0.664267, 0.725995),
            (-0.263171, 0.635351, 0.725995), (-0.34385, 0.595565, 0.725995), (-0.418645, 0.545589, 0.725995),
            (-0.486277, 0.486277, 0.725995), (-0.545589, 0.418645, 0.725995), (-0.595565, 0.34385, 0.725995),
            (-0.635351, 0.263171, 0.725995), (-0.664267, 0.17799, 0.725995), (-0.681816, 0.089763, 0.725995),
            (-0.687699, 0.0, 0.725995), (-0.681816, 0.089763, 0.725995), (-0.664267, 0.17799, 0.725995),
            (-0.635351, 0.263171, 0.725995), (-0.595565, 0.34385, 0.725995), (-0.545589, 0.418645, 0.725995),
            (-0.486277, 0.486277, 0.725995), (-0.418645, 0.545589, 0.725995), (-0.34385, 0.595565, 0.725995),
            (-0.263171, 0.635351, 0.725995), (-0.17799, 0.664267, 0.725995), (-0.089763, 0.681816, 0.725995),
            (0.0, 0.605174, 0.796093), (0.105087, 0.59598, 0.796093), (0.206982, 0.568678, 0.796093),
            (0.302587, 0.524096, 0.796093), (0.388998, 0.46359, 0.796093), (0.46359, 0.388998, 0.796093),
            (0.524096, 0.302587, 0.796093), (0.568678, 0.206982, 0.796093), (0.59598, 0.105087, 0.796093),
            (0.605174, 0.0, 0.796093), (0.59598, 0.105087, 0.796093), (0.568678, 0.206982, 0.796093),
            (0.524096, 0.302587, 0.796093), (0.46359, 0.388998, 0.796093), (0.388998, 0.46359, 0.796093),
            (0.302587, 0.524096, 0.796093), (0.206982, 0.568678, 0.796093), (0.105087, 0.59598, 0.796093),
            (0.0, 0.605174, 0.796093), (-0.105087, 0.59598, 0.796093), (-0.206982, 0.568678, 0.796093),
            (-0.302587, 0.524096, 0.796093), (-0.388998, 0.46359, 0.796093), (-0.46359, 0.388998, 0.796093),
            (-0.524096, 0.302587, 0.796093), (-0.568678, 0.206982, 0.796093), (-0.59598, 0.105087, 0.796093),
            (-0.605174, 0.0, 0.796093), (-0.59598, 0.105087, 0.796093), (-0.568678, 0.206982, 0.796093),
            (-0.524096, 0.302587, 0.796093), (-0.46359, 0.388998, 0.796093), (-0.388998, 0.46359, 0.796093),
            (-0.302587, 0.524096, 0.796093), (-0.206982, 0.568678, 0.796093), (-0.105087, 0.59598, 0.796093),
            (0.0, 0.515554, 0.856857), (0.089525, 0.507721, 0.856857), (0.17633, 0.484462, 0.856857),
            (0.257777, 0.446483, 0.856857), (0.331392, 0.394937, 0.856857), (0.394937, 0.331392, 0.856857),
            (0.446483, 0.257777, 0.856857), (0.484462, 0.17633, 0.856857), (0.507721, 0.089525, 0.856857),
            (0.515554, 0.0, 0.856857), (0.507721, 0.089525, 0.856857), (0.484462, 0.17633, 0.856857),
            (0.446483, 0.257777, 0.856857), (0.394937, 0.331392, 0.856857), (0.331392, 0.394937, 0.856857),
            (0.257777, 0.446483, 0.856857), (0.17633, 0.484462, 0.856857), (0.089525, 0.507721, 0.856857),
            (0.0, 0.515554, 0.856857), (-0.089525, 0.507721, 0.856857), (-0.17633, 0.484462, 0.856857),
            (-0.257777, 0.446483, 0.856857), (-0.331392, 0.394937, 0.856857), (-0.394937, 0.331392, 0.856857),
            (-0.446483, 0.257777, 0.856857), (-0.484462, 0.17633, 0.856857), (-0.507721, 0.089525, 0.856857),
            (-0.515554, 0.0, 0.856857), (-0.507721, 0.089525, 0.856857), (-0.484462, 0.17633, 0.856857),
            (-0.446483, 0.257777, 0.856857), (-0.394937, 0.331392, 0.856857), (-0.331392, 0.394937, 0.856857),
            (-0.257777, 0.446483, 0.856857), (-0.17633, 0.484462, 0.856857), (-0.089525, 0.507721, 0.856857),
            (0.0, 0.419889, 0.907575), (0.108675, 0.405582, 0.907575), (0.209945, 0.363635, 0.907575),
            (0.296906, 0.296906, 0.907575), (0.363635, 0.209945, 0.907575), (0.405582, 0.108675, 0.907575),
            (0.419889, 0.0, 0.907575), (0.405582, 0.108675, 0.907575), (0.363635, 0.209945, 0.907575),
            (0.296906, 0.296906, 0.907575), (0.209945, 0.363635, 0.907575), (0.108675, 0.405582, 0.907575),
            (0.0, 0.419889, 0.907575), (-0.108675, 0.405582, 0.907575), (-0.209945, 0.363635, 0.907575),
            (-0.296906, 0.296906, 0.907575), (-0.363635, 0.209945, 0.907575), (-0.405582, 0.108675, 0.907575),
            (-0.419889, 0.0, 0.907575), (-0.405582, 0.108675, 0.907575), (-0.363635, 0.209945, 0.907575),
            (-0.296906, 0.296906, 0.907575), (-0.209945, 0.363635, 0.907575), (-0.108675, 0.405582, 0.907575),
            (0.0, 0.319302, 0.947653), (0.082641, 0.308422, 0.947653), (0.159651, 0.276523, 0.947653),
            (0.22578, 0.22578, 0.947653), (0.276523, 0.159651, 0.947653), (0.308422, 0.082641, 0.947653),
            (0.319302, 0.0, 0.947653), (0.308422, 0.082641, 0.947653), (0.276523, 0.159651, 0.947653),
            (0.22578, 0.22578, 0.947653), (0.159651, 0.276523, 0.947653), (0.082641, 0.308422, 0.947653),
            (0.0, 0.319302, 0.947653), (-0.082641, 0.308422, 0.947653), (-0.159651, 0.276523, 0.947653),
            (-0.22578, 0.22578, 0.947653), (-0.276523, 0.159651, 0.947653), (-0.308422, 0.082641, 0.947653),
            (-0.319302, 0.0, 0.947653), (-0.308422, 0.082641, 0.947653), (-0.276523, 0.159651, 0.947653),
            (-0.22578, 0.22578, 0.947653), (-0.159651, 0.276523, 0.947653), (-0.082641, 0.308422, 0.947653),
            (0.0, 0.21497, 0.976621), (0.107485, 0.18617, 0.976621), (0.18617, 0.107485, 0.976621),
            (0.21497, 0.0, 0.976621), (0.18617, 0.107485, 0.976621), (0.107485, 0.18617, 0.976621),
            (0.0, 0.21497, 0.976621), (-0.107485, 0.18617, 0.976621), (-0.18617, 0.107485, 0.976621),
            (-0.21497, 0.0, 0.976621), (-0.18617, 0.107485, 0.976621), (-0.107485, 0.18617, 0.976621),
            (0.0, 0.108119, 0.994138), (0.05406, 0.093634, 0.994138), (0.093634, 0.05406, 0.994138),
            (0.108119, 0.0, 0.994138), (0.093634, 0.05406, 0.994138), (0.05406, 0.093634, 0.994138),
            (0.0, -0.108119, 0.994138), (-0.05406, -0.093634, 0.994138), (-0.093634, -0.05406, 0.994138),
            (-0.108119, 0.0, 0.994138), (-0.093634, 0.05406, 0.994138), (-0.05406, 0.093634, 0.994138),
            (0.0, 0.0, 1.0), (0.0, 0.0, 1.0), (0.0, 0.0, 1.0)
        )
        }

    def __len__(self):
        """Length of vectors."""
        return len(self.__vectors[self.__skyDensity])

    def __getitem__(self, key):
        """Get sky vector."""
        return self.__vectors[self.__skyDensity][key]

    def __iter__(self):
        """Iterat through sky vectors ."""
        return iter(self.__vectors[self.__skyDensity])
