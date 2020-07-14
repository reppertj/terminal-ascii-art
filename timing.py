import timeit
import asciiart

if __name__ == "__main__":
    filename = "sample.jpg"
    width = 80

    imarray = asciiart.initial_process(filename, width)

    n = 5

    normal_t = timeit.timeit(lambda: asciiart.brute_color_mask(imarray), number=n)
    # ~4.8s/run
    print(f"brute: {normal_t/n} per run")

    kdtree_t = timeit.timeit(lambda: asciiart.tree_color_mask(imarray), number=n)

    # ~0.34s/run - >14x speedup!
    print(f"kd-tree: {kdtree_t/n} per run")
