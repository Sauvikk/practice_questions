class minStepsInfiniteGrid:

  def coverPoints(self, X, Y):
        totalStep = 0
        currentX = X[0]
        currentY = Y[0]
        for i in range(1, len(X)):
            totalStep += max(abs(currentX - X[i]), abs(currentY - Y[i]))
            currentX = X[i]
            currentY = Y[i]
        return totalStep

minSteps = minStepsInfiniteGrid()
x = [0, 1, 1]
y = [0, 1, 2]

# in co-ordinate form [(0, 0), (1, 1), (1, 2)]


res = minSteps.coverPoints(x, y)
print(res)
