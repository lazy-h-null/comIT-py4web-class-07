# Last time modified: 03/04/26
# Authour: lazy-h-null
# Class 07 - Assignment 1

def generate_website():
    html_base = ""

    with open("garbage.html", "r") as website:
        html_base = website.read()
        
    page_title = "MY Awesome Python Website"

    html_modified = html_base.replace("<title>Document", f"<title>{page_title}") 

    daisy_ui ="""

    <!-- Daisy UI -->
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
    <!-- Daisy ui themes -->
    <link href="https://cdn.jsdelivr.net/npm/daisyui@5/themes.css" rel="stylesheet" type="text/css" />

    """

    html_modified = html_modified.replace("</head>", daisy_ui +"\n</head>" )

    theme = "cyberpunk"
    html_modified = html_modified.replace('<html lang="en">', f'<html lang="en" data-theme="{theme}">')

    nav_bar = """
    <div class="navbar bg-base-100 shadow-sm">
      <a class="btn btn-ghost text-xl">My Python Web</a>
    </div>
    """
    my_table = """
    <div class="overflow-x-auto rounded-box border border-base-content/5 bg-base-100">
    <table class="table">
    <!-- head -->
    <thead>
      <tr>
        <th></th>
        <th>Name</th>
        <th>Job</th>
        <th>Favorite Color</th>
      </tr>
    </thead>
    <tbody>
      <!-- row 1 -->
      <tr>
        <th>1</th>
        <td>Cy Ganderton</td>
        <td>Quality Control Specialist</td>
        <td>Blue</td>
      </tr>
      <!-- row 2 -->
      <tr>
        <th>2</th>
        <td>Hart Hagerty</td>
        <td>Desktop Support Technician</td>
        <td>Purple</td>
      </tr>
      <!-- row 3 -->
      <tr>
        <th>3</th>
        <td>Brice Swyre</td>
        <td>Tax Accountant</td>
        <td>Red</td>
      </tr>
    </tbody>
    </table>
    </div>
    """

    my_stack = """
    <div class="container mx-auto px-4 mb-10 text-center">
        <h2 class="text-2xl font-bold mb-4">Image Stack View</h2>
        <div class="stack w-48 mx-auto">
          <img src="https://img.daisyui.com/images/stock/photo-1572635148818-ef6fd45eb394.webp" class="rounded-box" />
          <img src="https://img.daisyui.com/images/stock/photo-1565098772267-60af42b81ef2.webp" class="rounded-box" />
          <img src="https://img.daisyui.com/images/stock/photo-1559703248-dcaaec9fab78.webp" class="rounded-box" />
        </div>
    </div>
    """
    html_modified = html_modified.replace('<body>', '<body>\n'+nav_bar)
    html_modified = html_modified.replace('</body>', my_stack + my_table + "\n</body>")

    with open("index.html", "w") as file:
        file.write(html_modified)

generate_website()