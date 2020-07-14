from scipy.spatial import cKDTree


class ANSITree:
    def __init__(self, ansi_dict):
        self.ansi_values = list(ansi_dict.keys())
        colors = [rgb for key, rgb in ansi_dict.items()]
        self.tree = cKDTree(colors)

    def nearest_ansi(self, color):
        idx = self.tree.query(color, p=2)[1]
        return self.ansi_values[idx]
