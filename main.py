import cv2

# Charger l'image
img = cv2.imread("image.jpg")

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Appliquer un seuil pour mettre en évidence les zones les plus lumineuses
_, threshold = cv2.threshold(gray, 253, 255, cv2.THRESH_BINARY)

# Trouver les contours des zones lumineuses
contours, _ = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Dessiner un rectangle autour des contours des zones lumineuses
for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Afficher l'image avec les rectangles
cv2.imshow("Bright spots", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
