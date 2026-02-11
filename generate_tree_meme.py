#!/usr/bin/env python3
"""
Script to generate a humorous meme comparing real trees with CS data structure trees.
The meme follows the "What I want vs What I have" format.
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_tree_meme():
    # Image dimensions
    width = 1200
    height = 800
    
    # Create new image with white background
    img = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(img)
    
    # Try to use a nice font, fall back to default if not available
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 48)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        text_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        tree_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 20)
    except:
        # Fall back to default font
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        tree_font = ImageFont.load_default()
    
    # Draw title at top
    title = "THE TREE STRUGGLE IS REAL"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    draw.text((title_x, 30), title, fill='black', font=title_font)
    
    # Divide image into two halves
    left_half_x = 0
    right_half_x = width // 2
    content_y = 120
    
    # LEFT SIDE - "Tree I want" (Real tree)
    # Draw green background for left side
    draw.rectangle([left_half_x, content_y, right_half_x - 10, height], fill='#90EE90', outline='black', width=3)
    
    # Label for left side
    left_label = "Tree I want 🌳"
    left_label_bbox = draw.textbbox((0, 0), left_label, font=label_font)
    left_label_width = left_label_bbox[2] - left_label_bbox[0]
    left_label_x = left_half_x + (right_half_x - 10 - left_half_x - left_label_width) // 2
    draw.text((left_label_x, content_y + 20), left_label, fill='darkgreen', font=label_font)
    
    # Draw a nice ASCII art tree
    tree_art = """
          🌲
         /|\\
        / | \\
       /  |  \\
      /   |   \\
     /    |    \\
    /_____|_____\\
          |
          |
    """
    
    # Draw the tree art
    tree_y = content_y + 100
    for line in tree_art.strip().split('\n'):
        line_bbox = draw.textbbox((0, 0), line, font=tree_font)
        line_width = line_bbox[2] - line_bbox[0]
        line_x = left_half_x + (right_half_x - 10 - left_half_x - line_width) // 2
        draw.text((line_x, tree_y), line, fill='darkgreen', font=tree_font)
        tree_y += 35
    
    # Add descriptive text
    desc_text = "Fresh air, nature,\npeace & quiet"
    desc_y = tree_y + 40
    for line in desc_text.split('\n'):
        line_bbox = draw.textbbox((0, 0), line, font=text_font)
        line_width = line_bbox[2] - line_bbox[0]
        line_x = left_half_x + (right_half_x - 10 - left_half_x - line_width) // 2
        draw.text((line_x, desc_y), line, fill='darkgreen', font=text_font)
        desc_y += 40
    
    # RIGHT SIDE - "Trees I have" (CS trees)
    # Draw red/pink background for right side
    draw.rectangle([right_half_x + 10, content_y, width, height], fill='#FFB6C6', outline='black', width=3)
    
    # Label for right side
    right_label = "Trees I have 💻"
    right_label_bbox = draw.textbbox((0, 0), right_label, font=label_font)
    right_label_width = right_label_bbox[2] - right_label_bbox[0]
    right_label_x = right_half_x + 10 + (width - right_half_x - 10 - right_label_width) // 2
    draw.text((right_label_x, content_y + 20), right_label, fill='darkred', font=label_font)
    
    # List of CS trees
    cs_trees = [
        "• B-tree",
        "• Red-black tree",
        "• K-D tree",
        "• Range tree",
        "• AVL tree",
        "• Binary Search Tree",
        "• Segment tree",
        "• Trie"
    ]
    
    cs_y = content_y + 100
    for tree_name in cs_trees:
        draw.text((right_half_x + 80, cs_y), tree_name, fill='darkred', font=text_font)
        cs_y += 50
    
    # Add a simple tree structure diagram
    diagram = """
        ┌─┐
        │*│
        └┬┘
      ┌──┴──┐
      │     │
     ┌┴┐   ┌┴┐
     │ │   │ │
     └─┘   └─┘
    """
    
    diagram_y = cs_y + 30
    for line in diagram.strip().split('\n'):
        line_bbox = draw.textbbox((0, 0), line, font=tree_font)
        line_width = line_bbox[2] - line_bbox[0]
        line_x = right_half_x + 10 + (width - right_half_x - 10 - line_width) // 2
        draw.text((line_x, diagram_y), line, fill='darkred', font=tree_font)
        diagram_y += 25
    
    # Save the image
    output_path = os.path.join(os.path.dirname(__file__), 'public', 'tree-meme.png')
    img.save(output_path, 'PNG')
    print(f"Meme successfully created at: {output_path}")
    
    return output_path

if __name__ == '__main__':
    create_tree_meme()
