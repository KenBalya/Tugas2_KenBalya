# Tugas1
 1. Alur mengimplementasikan checklist:
    a. Membuat directory baru bernama Tugas1 beserta repositori github
    b. Membuat project django baru dengan nama movie_list dengan command: django-admin startproject movie_list
    c. Membuat aplikasi bernama 'main' pada project tersebut dengan command: manage.py startapp main
    d. Menambahkan 'main' pada installed_apps di settings.py
    e. Membuat folder baru di dalam folder main dengan nama templates
    f. Menambahkan file main.html pada template 
    g. Membuat class baru pada models.py dengan nama 'Movie' dengan atribut berupa name, release_date, rating, dan likes
    h. Melakukan models migration 
    i. Membuat routing yang menghubungkan views dengan template html
    j. Menjalankan aplikasi dengan command: manage.py runserver
    k. Membuka halaman pada: http://127.0.0.1:8000/main/

2. Bagan dapat dilihat pada tautan berikut: ![Alt text](image.png)

3. Virtual environment adalah sebuah sistem yang dapat membuat pengguna melakukan interaksi terhadap lingkungan program maupun dengan pengguna lainnya. Sebuah aplikasi bisa saja dibuat tanpa VE, akan tetapi pengerjaannya tidak efisien.

4. 
    a. MVC atau Model-View-Controller adalah sebuah pola desain pada pengembangan sebuah aplikasi atau perangkat lunak yang terdiri dari bagian model, view, dan controller. Design Pattern ini digunakan pada beberapa framework seperti Laravel dan CodeIgniter. 
    b. MVT atau Model-View-Tempate juga merupakan pola desain yang mirip dengan MVC. Hanya saja perbedaannya adalah pada MVT, bagian controller sudah dihandle oleh framework sehingga programmer hanya perlu memperhatikan presentasi dari konten aplikasi yang disebut dengan template.MVT digunakan oleh framework seperti django.
    c. MVVP atau Model-View-ViewModel merupakan pola desain yang serupa dengan MVC hanya saja terdapat sebuah perubahan pada bagian controller yaitu pemisahan antara pengembangan front-end dan back-end. Framework yang menggunakan MVVC adalah Prism.

    Secara umum, perbedaan ketiga design pattern tersebut terdapat pada bagaimana cara menampilkan data pada view. Pada MVC, controller berfungsi sebagai jembatan antara model dan views yang berfungsi untuk menentukan bagaimana data yang di-fetch akan ditampilkan dengan basis logika yang sama. Sementara pada MVVC, basis logika yang digunakan pada server-side dan client-side berbeda. Sedangkan pada MVT view berfungsi sebagai tempat transit bagi data yang kemudian akan ditransfer ke halaman yang sudah ditentukan pada template untuk ditampilkan pada client.

Tugas 3:
     
     1. Secara umum, perbedaan antara POST dan GET dapat terlihat pada URL. Dimana pada method GET, data akan terlihat pada URL dan sebaliknya pada method POST. Apabila ditinjau dari fungsionalitasnya secara khusus pada django, GET bersifat indempoten sementara POST tidak. Selain itu, dalam melakukan GET request di django tidak diperlukan validasi dan sebaliknya jika menggunakan POST.

     2. Perbedaan antara ketiganya terlihat pada purpose/tujuan pemakaian data delivery tersebut. Apabila seseorang menginginkan kemudahan pada prosesnya, maka gunakan JSON karena JSON memiliki struktur yang sederhana. Apabila menginginkan fleksibilitas, pilih XML. Dan apabila hendak menampilkan data tersebut pada client-side, maka harus menggunakan HTML untuk menampilkan data dengan format yang lebih presentatif.

     3. Aplikasi modern biasanya memiliki kompleksitas data yang tinggi sehingga dibutuhkan struktur data delivery yang sederhana seperti JSON.

     4. Untuk mengimplementasikan checklist diatas, saya membuatnya dengan mengikuti tutorial beserta beberapa sumber lainnya. Hal itu dikarenakan beberapa data yang saya miliki tidak sama strukturnya dengan yang di tutorial sehingga perlu memiliki atribut sendiri dan proses pengolahan sendiri.
