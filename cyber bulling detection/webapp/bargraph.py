import numpy as np
import matplotlib.pyplot as plt


## set width of bar
class bargraph:
    def view(d, img):
        try:
            a1 = []
            a2 = []
            a3 = []
            a4 = []
            algo = []

            for r in d:
                print(r)
                algo.append(r)
                a1.append(round(float(d[r][0]), 2))
                a2.append(round(float(d[r][1]), 2))
                a3.append(round(float(d[r][2]), 2))
                a4.append(round(float(d[r][3]), 2))

            k = []
            v = []
            barWidth = 0.25
            fig = plt.subplots(figsize=(10, 7))
            br1 = np.arange(len(a1))
            br2 = [x + barWidth for x in br1]
            br3 = [x + barWidth for x in br2]
            br4 = [x + barWidth for x in br3]

            print(a1, a2)
            plt.bar(br1, a1, color='r', width=barWidth,
                    edgecolor='grey', label='Accuracy')
            plt.bar(br2, a2, color='g', width=barWidth,
                    edgecolor='grey', label='Precision')
            plt.bar(br3, a3, color='y', width=barWidth,
                    edgecolor='grey', label='Recall')
            plt.bar(br4, a4, color='b', width=barWidth,
                    edgecolor='grey', label='F1')
            plt.xlabel('Algorithms ', fontweight='bold', fontsize=15)
            plt.ylabel('Accuracy', fontweight='bold', fontsize=15)
            plt.xticks([r + barWidth for r in range(len(a1))], algo)
            plt.legend()
            plt.savefig(img, dpi=(200))
        except:
            pass
        from PIL import Image
        im = Image.open(r''+str(img)+'')
        im.show()


if __name__ == '__main__':
    bargraph.view({'a1': [1, 2, 3, 4], 'a2': [1, 2, 3, 4], 'a3': [1, 2, 3, 4]},'g1.jpg')
