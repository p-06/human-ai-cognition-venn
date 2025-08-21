import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Create figure
fig, ax = plt.subplots(figsize=(8, 6))

# Define Venn diagram (Human vs AI Cognition)
venn = venn2(subsets=(1, 1, 1), set_labels=("Human Cognition", "AI Cognition"), ax=ax)

# Colors for the circles
venn.get_patch_by_id('10').set_color("lightblue")   # Human unique
venn.get_patch_by_id('01').set_color("lightgreen")  # AI unique
venn.get_patch_by_id('11').set_color("turquoise")   # Overlap zone
venn.get_patch_by_id('10').set_alpha(0.7)
venn.get_patch_by_id('01').set_alpha(0.7)
venn.get_patch_by_id('11').set_alpha(0.8)

# Customize labels
venn.get_label_by_id('10').set_text(
    "Rationality\nEmotions\nCreativity\nEthics\nSelf-awareness"
)
venn.get_label_by_id('01').set_text(
    "Pattern recognition\nOptimization\nSimulation\nHigh speed\nNo self-awareness"
)
venn.get_label_by_id('11').set_text(
    "Efficiency\nProblem-solving"
)

# Adjust title
plt.title("Human Cognition vs AI Cognition", fontsize=16, fontweight="bold")

# Save and show
plt.tight_layout()
plt.savefig("human_vs_ai_cognition.png", dpi=300)
plt.show()
