model = load_model("ASLModel.h5")

loss, acc = model.evaluate(X_test, y_test)
print("Loss = ", loss)
print("Accuracy = ", acc)