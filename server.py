import os

def generate_html():
    # Input data dari pengguna
    title = input("Masukkan judul: ")
    desc = input("Masukkan deskripsi: ")
    url = input("Masukkan URL: ")
    image = input("Masukkan URL gambar: ")
    file_name = input("Masukkan nama file HTML: ")

    # Menentukan path ke folder "posts"
    folder_path = "posts"
    
    # Membuat folder "posts" jika belum ada
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Menyusun path lengkap untuk file HTML
    full_file_path = os.path.join(folder_path, file_name)

    # Konten HTML
    html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZwTl"
        crossorigin="anonymous">

    <!-- Meta Tags -->
    <meta property="og:type" content="article" />
    <meta property="og:image" content="{image}" />
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{desc}" />
    <meta property="og:url" content="{url}" />
    <meta property="og:site_name" content="bobwatcherx.github.io" />

</head>
<body>

    <!-- CONTENT -->
    <div class="container mt-5">
        <img src="{image}" style="width:100%;height: 300px; background-size: cover;" alt="">
        <br>
        <h3>Klik DI bawah ini Untuk Menonton Video</h3>
        <br>
        <a href="{url}" style="background-color: blue;color:white;text-decoration: none;padding: 10px;">KLIK DISINI UNTUK MENONTON</a>
    </div>
    <br>
    <!-- Iklan -->
    <div class="container mt-5" id="iklanContainer"></div>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
        crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
        integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
        crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
        integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
        crossorigin="anonymous"></script>

    <script src="js/main.js"></script>

</body>
</html>
'''

    # Menulis ke file HTML
    with open(full_file_path, 'w') as html_file:
        html_file.write(html_content)

# Panggil fungsi untuk menghasilkan HTML
generate_html()
