from PIL import Image, ImageDraw, ImageFont

# Load the original image and the rating icon
original_image = Image.open('image_case2.jpg')
rating_icon = Image.open('rating_excellent.png')

# ICON
icon_size = (20, 20)
rating_icon = rating_icon.resize(icon_size)

# Create a draw object to edit the image
draw = ImageDraw.Draw(original_image)

# Size and colors for the rectangles
orange_rect_color = (255, 165, 0)  # Orange color
white_rect_color = (255, 255, 255)  # White color
orange_rect_size = (100, 40)  # Size of the orange rectangle
white_rect_size = (140, 40)  # Size of the white rectangle for 'all items'
rating_rect_size = (160, 40)  # Enlarged size of the white rectangle for '91% (+500)'
corner_radius = 10  # Radius for rounded corners

# Positions for the rectangles
orange_rect_position = (20, 20)  # Position for the orange rectangle
white_rect_position = (orange_rect_position[0] + orange_rect_size[0] - 18, orange_rect_position[1])
rating_rect_position = (original_image.width - rating_rect_size[0] - 20, original_image.height - rating_rect_size[1] - 20)

# Draw the rounded rectangles
draw.rounded_rectangle([orange_rect_position, (orange_rect_position[0] + orange_rect_size[0], orange_rect_position[1] + orange_rect_size[1])], radius=corner_radius, fill=orange_rect_color)
draw.rounded_rectangle([white_rect_position, (white_rect_position[0] + white_rect_size[0], white_rect_position[1] + white_rect_size[1])], radius=corner_radius, fill=white_rect_color)
draw.rounded_rectangle([rating_rect_position, (rating_rect_position[0] + rating_rect_size[0], rating_rect_position[1] + rating_rect_size[1])], radius=corner_radius, fill=white_rect_color)

# Fonts
font_path = 'arialbd.ttf'
font_size = 20
font = ImageFont.truetype(font_path, font_size)
small_font = ImageFont.truetype(font_path, 18)  # Smaller font for '(500+)'

# Text and colors
discount_text = "-20%"
items_text = "all items"
rating_text = "91%"
reviews_text = "(500+)"
text_color = (0, 0, 0)  # Black color for the text
soft_text_color = (128, 128, 128)  # Soft grey color

# Text positions
discount_text_position = (
    orange_rect_position[0] + (orange_rect_size[0] - len(discount_text) * font_size / 2) / 2,
    orange_rect_position[1] + (orange_rect_size[1] - font_size) / 2
)
items_text_position = (
    white_rect_position[0] + (white_rect_size[0] - len(items_text) * 18 / 2) / 2,
    white_rect_position[1] + (white_rect_size[1] - 18) / 2
)
icon_position = (
    int(rating_rect_position[0] + 10),
    int(rating_rect_position[1] + (rating_rect_size[1] - icon_size[1]) / 2)
)

# Calculate space needed for "91%"
approx_char_width = font_size // 2
rating_text_length = len(rating_text) * approx_char_width

# Position for "91%" and "(500+)"
rating_text_position = (
    int(icon_position[0] + icon_size[0] + 5),
    int(rating_rect_position[1] + (rating_rect_size[1] - font_size) / 2)
)
reviews_text_position = (
    int(rating_text_position[0] + rating_text_length + 16),
    int(rating_text_position[1])
)

# Draw the texts on the rectangles
draw.text(discount_text_position, discount_text, font=font, fill=text_color)
draw.text(items_text_position, items_text, font=small_font, fill=text_color)
original_image.paste(rating_icon, icon_position, rating_icon)
draw.text(rating_text_position, rating_text, font=font, fill=text_color)
draw.text(reviews_text_position, reviews_text, font=small_font, fill=soft_text_color)

# Save the edited image
edited_image_path = 'edited_image_final22.png'
original_image.save(edited_image_path)

print(f"Image saved to {edited_image_path}")
