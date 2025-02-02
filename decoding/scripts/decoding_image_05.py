import cv2
from pyzbar.pyzbar import decode
import numpy as np
import zxing
# Initialize the ZXing reader
reader = zxing.BarCodeReader()
# Load the Aztec code image
image_path = "../images/source/image_05.png"  # Replace with your image path
image = cv2.imread(image_path)
# Decode the Aztec code using ZXing
decoded = reader.decode(image_path)
# Check if the Aztec code was successfully decoded
if decoded:
    print(f"Decoded Data: {decoded.parsed}")
    print(f"Barcode Format: {decoded.format}")
    # Check if points are available
    if hasattr(decoded, "points") and decoded.points:
        try:
            points = np.array(decoded.points, dtype=np.int32).reshape((-1, 1, 2))  # Ensure proper shape
            cv2.polylines(image, [points], isClosed=True, color=(0, 255, 0), thickness=2)
            # Annotate the decoded data beside the bounding box
            x, y = points[0][0]  # Extract x, y coordinates
            cv2.putText(image, decoded.parsed, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        except Exception as e:
            print(f"Error processing bounding box: {e}")
    # Display the image with the Aztec code highlighted and annotated
    cv2.imshow("Aztec Code with Annotation", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # Save the annotated image
    output_file = "../images/decoded/decoded_aztec.png"
    cv2.imwrite(output_file, image)
    print(f"Annotated image saved as {output_file}")
else:
    print("Failed to decode the Aztec code.")