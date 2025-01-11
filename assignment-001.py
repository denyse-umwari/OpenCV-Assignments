#Import opencv
import cv2

# Load and resize the image
image = cv2.imread('assignment-001-given.jpg')
resized_image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))

# Draw a green rectangle around the plate
cv2.rectangle(resized_image, (130, 90), (500, 470), (0, 255, 0), 3)

# Plate number text
plate_number = "RAH972U"

# Create a semi-transparent rectangle for the background
overlay = resized_image.copy()
cv2.rectangle(overlay, (400, 20), (600, 80), (0, 0, 0), -1)

# Apply transparency using addWeighted
alpha = 0.6
cv2.addWeighted(overlay, alpha, resized_image, 1 - alpha, 0, resized_image)

# Put the text inside the rectangle
cv2.putText(resized_image, plate_number, (420, 65), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

# Display the image
cv2.imshow("Image", resized_image)

# Save the final image to a new file
cv2.imwrite('assignment-001-result.jpg', resized_image)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
