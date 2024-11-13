from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


def main():
    # 0 = dog, 1 = cat, 2 = bird
    data_labels = ['dog', 'cat', 'bird']  # import 4 images of each
    # "Rrun" four images of dogs cats bird each
    actual_results = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
    prediction = [2, 2, 0, 1, 1, 1, 1, 1, 2, 2, 0, 2]
    ideal_results = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2]
    print(f'''Accuracy = {
        (accuracy_score(actual_results, prediction))*100:.2f}''')
    print(f'Confusion Matrix:\n{confusion_matrix(actual_results, prediction)}')

    # Generate a confusion matrix for Ideal Matrix
    cm = confusion_matrix(actual_results, ideal_results)
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm, display_labels=data_labels)
    disp.plot()
    plt.title('Confusion matrix')
    plt.show()

    # Generate a confusion matrix for prediction Matrix
    cm2 = confusion_matrix(actual_results, prediction)
    disp = ConfusionMatrixDisplay(
        confusion_matrix=cm2, display_labels=data_labels)
    plt.title('Confusion matrix prediction')
    plt.show()


if __name__ == '__main__':
    main()
