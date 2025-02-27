"""Script for documenting the Landscape Model xNTTP model variant."""
import os
import base.documentation

root_folder = os.path.abspath(os.path.join(os.path.dirname(base.__file__), ".."))
base.documentation.write_contribution_notes(os.path.join(root_folder, "..", "..", "CONTRIBUTING.md"))
base.documentation.document_variant(
    os.path.join(root_folder, "..", "variant", "variant_readme_template.md"),
    os.path.join(root_folder, "..", "..", "README.md"),
    "xNTTP",
    "https://github.com/xlandscape/xNTTP"
)
