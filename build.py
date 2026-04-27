#!/usr/bin/env python3
"""Build multi-page EazyFarms site from shared template parts."""

# ============ SHARED HEAD ============
HEAD = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>__TITLE__</title>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&family=Playfair+Display:wght@700;800&display=swap" rel="stylesheet" />

  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
  <link rel="stylesheet" href="https://unpkg.com/aos@2.3.4/dist/aos.css" />
  <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>

  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: { sans: ['Poppins', 'sans-serif'], serif: ['Playfair Display', 'serif'] },
          colors: {
            forest: { 50:'#f0fdf0',100:'#dcfce7',200:'#bbf7d0',300:'#86efac',400:'#4ade80',500:'#22c55e',600:'#16a34a',700:'#15803d',800:'#166534',900:'#14532d' },
            amber:  { 400:'#fbbf24',500:'#f59e0b' },
            brown:  { 50:'#faf6f1',100:'#f0e6d6',200:'#d9c4a3',300:'#b8936a',400:'#9a6f3f',500:'#7a5430',600:'#5f3f22',700:'#4a3019',800:'#2f1e0f' }
          }
        }
      }
    }
  </script>

  <style>
    *{scroll-behavior:smooth} body{font-family:'Poppins',sans-serif}
    .glass{background:rgba(255,255,255,.1);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);border:1px solid rgba(255,255,255,.18)}
    .gradient-text{background:linear-gradient(135deg,#22c55e,#86efac);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
    .gradient-text-gold{background:linear-gradient(135deg,#b8936a,#f0e6d6);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
    .hero-bg{background-image:linear-gradient(135deg,rgba(10,30,10,.78) 0%,rgba(20,83,45,.55) 100%),url('hens-factory-chicken-cages.jpg');background-size:cover;background-position:center;background-attachment:fixed}
    .page-hero{background-image:linear-gradient(135deg,rgba(10,30,10,.82) 0%,rgba(20,83,45,.65) 100%),url('woman-getting-eggs-supermarket.jpg');background-size:cover;background-position:center}
    .btn-shine{position:relative;overflow:hidden}
    .btn-shine::after{content:'';position:absolute;top:-50%;left:-75%;width:50%;height:200%;background:rgba(255,255,255,.2);transform:skewX(-25deg);transition:left .5s}
    .btn-shine:hover::after{left:125%}
    .card-lift{transition:transform .3s cubic-bezier(.25,.8,.25,1),box-shadow .3s cubic-bezier(.25,.8,.25,1)}
    .card-lift:hover{transform:translateY(-8px);box-shadow:0 20px 60px rgba(0,0,0,.15)}
    .animated-underline{position:relative}
    .animated-underline::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:3px;background:linear-gradient(90deg,#22c55e,#86efac);border-radius:2px;transition:width .4s ease}
    .animated-underline:hover::after,.nav-link-active::after{width:100%}
    .nav-link-active{color:#15803d!important}
    ::-webkit-scrollbar{width:6px}::-webkit-scrollbar-track{background:#f1f1f1}::-webkit-scrollbar-thumb{background:#16a34a;border-radius:3px}
    @keyframes pulse-green{0%,100%{box-shadow:0 0 0 0 rgba(34,197,94,.5)}50%{box-shadow:0 0 0 10px rgba(34,197,94,0)}}
    .pulse-dot{animation:pulse-green 2s infinite}
    @keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
    .float-anim{animation:float 4s ease-in-out infinite}
    .nav-scrolled{background:rgba(255,255,255,.97)!important;box-shadow:0 2px 20px rgba(0,0,0,.08)!important}
    .img-overlay{position:relative;overflow:hidden}
    .img-overlay::after{content:'';position:absolute;inset:0;background:linear-gradient(to top,rgba(0,0,0,.4) 0%,transparent 60%)}
    .img-overlay img{transition:transform .6s ease}
    .img-overlay:hover img{transform:scale(1.07)}
    .form-input:focus{outline:none;border-color:#16a34a;box-shadow:0 0 0 4px rgba(22,163,74,.15)}
    .pay-card input:checked + .pay-inner{border-color:#16a34a;background:#f0fdf0;color:#15803d}
    .pay-inner{border:2px solid #e5e7eb;border-radius:10px;padding:.75rem 1rem;cursor:pointer;transition:all .2s;display:flex;align-items:center;gap:.5rem;font-weight:500}
    .pay-inner:hover{border-color:#16a34a;background:#f0fdf0}
    [x-cloak]{display:none!important}
  </style>
</head>"""

# ============ NAV ============
def nav(active):
    """active is one of: home, about, products, delivery, order, contact"""
    items = [
        ("home", "Home", "index.html"),
        ("about", "About", "about.html"),
        ("products", "Products", "products.html"),
        ("delivery", "Delivery", "delivery.html"),
        ("contact", "Contact", "contact.html"),
    ]
    links = ""
    for key, label, href in items:
        cls = "animated-underline text-sm font-semibold transition-colors text-gray-700 hover:text-forest-700"
        if key == active:
            cls += " nav-link-active"
        links += f'        <li><a href="{href}" class="{cls}">{label}</a></li>\n'

    return f"""<body class="bg-white text-gray-800" x-data="{{ mobileOpen: false }}">

<nav class="fixed top-0 inset-x-0 z-50 transition-all duration-300 py-3 px-6 md:px-10 nav-scrolled">
  <div class="max-w-7xl mx-auto flex items-center justify-between">
    <a href="index.html" class="flex items-center gap-2.5">
      <img src="easyfarms%20logo.jpg" alt="Eazy Farms Logo" class="w-11 h-11 rounded-xl object-cover shadow-md ring-2 ring-forest-100" />
      <span class="text-xl font-black text-forest-800">Eazy<span class="text-brown-500">Farms</span></span>
    </a>
    <div class="flex items-center gap-8">
      <ul class="hidden md:flex items-center gap-7">
{links.rstrip()}
      </ul>
      <a href="order.html" class="hidden md:inline-flex items-center gap-2 bg-forest-600 hover:bg-forest-500 text-white text-sm font-bold px-5 py-2.5 rounded-full shadow-lg transition-all btn-shine">
        <i class="fa-solid fa-cart-shopping text-xs"></i> Order Now
      </a>
      <button class="md:hidden p-2 rounded-lg text-gray-700" @click="mobileOpen = !mobileOpen"><i class="fa-solid fa-bars text-lg"></i></button>
    </div>
  </div>
  <div x-show="mobileOpen" x-transition x-cloak class="md:hidden mt-3 bg-white rounded-2xl shadow-2xl p-5 mx-0">
    <ul class="space-y-3">
      <li><a href="index.html" class="block text-gray-700 font-semibold hover:text-forest-700 py-1">Home</a></li>
      <li><a href="about.html" class="block text-gray-700 font-semibold hover:text-forest-700 py-1">About</a></li>
      <li><a href="products.html" class="block text-gray-700 font-semibold hover:text-forest-700 py-1">Products</a></li>
      <li><a href="delivery.html" class="block text-gray-700 font-semibold hover:text-forest-700 py-1">Delivery</a></li>
      <li><a href="order.html" class="block text-gray-700 font-semibold hover:text-forest-700 py-1">Order</a></li>
      <li><a href="contact.html" class="block text-gray-700 font-semibold hover:text-forest-700 py-1">Contact</a></li>
    </ul>
  </div>
</nav>
"""

# ============ PAGE TITLE BANNER ============
def page_banner(title, subtitle, breadcrumb):
    return f"""
<section class="page-hero pt-32 pb-16 px-6 md:px-10">
  <div class="max-w-7xl mx-auto text-center">
    <p class="text-brown-200 text-xs font-bold uppercase tracking-widest mb-3">{breadcrumb}</p>
    <h1 class="font-serif text-4xl md:text-6xl font-black text-white mb-4">{title}</h1>
    <p class="text-white/80 max-w-xl mx-auto">{subtitle}</p>
  </div>
</section>
"""

# ============ FOOTER ============
FOOTER = """
<footer class="bg-gray-950 text-gray-400 pt-14 pb-8 px-6 md:px-10">
  <div class="max-w-7xl mx-auto grid md:grid-cols-4 gap-10 mb-10">
    <div class="md:col-span-2">
      <div class="flex items-center gap-2.5 mb-4">
        <img src="easyfarms%20logo.jpg" alt="Eazy Farms Logo" class="w-10 h-10 rounded-lg object-cover ring-2 ring-white/30" />
        <span class="text-white font-black text-xl">Eazy<span class="text-brown-300">Farms</span></span>
      </div>
      <p class="text-sm leading-relaxed max-w-sm">Rwanda's climate-smart poultry business. Fresh, affordable eggs delivered within 48–72 hours through sustainable practices.</p>
    </div>
    <div>
      <h4 class="text-white font-bold mb-4 text-sm uppercase tracking-wider">Explore</h4>
      <ul class="space-y-2 text-sm">
        <li><a href="index.html" class="hover:text-forest-400 transition-colors">Home</a></li>
        <li><a href="about.html" class="hover:text-forest-400 transition-colors">About</a></li>
        <li><a href="products.html" class="hover:text-forest-400 transition-colors">Products</a></li>
        <li><a href="delivery.html" class="hover:text-forest-400 transition-colors">Delivery</a></li>
        <li><a href="order.html" class="hover:text-forest-400 transition-colors">Order</a></li>
        <li><a href="contact.html" class="hover:text-forest-400 transition-colors">Contact</a></li>
      </ul>
    </div>
    <div>
      <h4 class="text-white font-bold mb-4 text-sm uppercase tracking-wider">Get In Touch</h4>
      <ul class="space-y-2 text-sm">
        <li><i class="fa-solid fa-phone text-forest-400 mr-2"></i><a href="tel:+250798287234" class="hover:text-white">+250 798 287 234</a></li>
        <li><i class="fa-solid fa-envelope text-forest-400 mr-2"></i><a href="mailto:akotonimohchristine@gmail.com" class="hover:text-white break-all">akotonimohchristine@gmail.com</a></li>
        <li><i class="fa-solid fa-location-dot text-forest-400 mr-2"></i>Eastern Province, Rwanda</li>
      </ul>
    </div>
  </div>
  <div class="border-t border-gray-800 pt-6 text-center text-xs text-gray-500">
    &copy; 2026 EazyFarms. All rights reserved.
  </div>
</footer>

<script src="https://unpkg.com/aos@2.3.4/dist/aos.js"></script>
<script>
  AOS.init({ once: true, easing: 'ease-out-cubic', offset: 60 });
  const d = document.getElementById('date');
  if (d) d.min = new Date().toISOString().split('T')[0];
</script>
</body>
</html>
"""

# ============ PAGE BODIES ============

HOME_BODY = """
<section id="home" class="hero-bg min-h-[92vh] flex items-center relative">
  <div class="absolute top-1/4 right-10 w-72 h-72 bg-forest-500/10 rounded-full blur-3xl pointer-events-none"></div>
  <div class="absolute bottom-1/4 left-10 w-56 h-56 bg-brown-300/10 rounded-full blur-3xl pointer-events-none"></div>

  <div class="max-w-7xl mx-auto w-full px-6 md:px-10 pt-24 pb-16 grid md:grid-cols-2 gap-12 items-center">
    <div data-aos="fade-right" data-aos-duration="900">
      <div class="inline-flex items-center gap-2 bg-white/10 backdrop-blur border border-white/20 text-brown-200 text-xs font-bold px-4 py-1.5 rounded-full mb-6 uppercase tracking-widest">
        <span class="w-2 h-2 bg-brown-300 rounded-full pulse-dot"></span>
        Rwanda's Climate-Smart Farm
      </div>
      <h1 class="font-serif text-5xl md:text-6xl lg:text-7xl font-black text-white leading-tight mb-6">
        Fresh.<br /><span class="gradient-text-gold">Reliable.</span><br />Sustainable.
      </h1>
      <p class="text-white/80 text-lg max-w-md mb-8 leading-relaxed">
        Advancing food security in Rwanda through climate-smart egg production — delivered to your door within <strong class="text-white">48–72 hours</strong>.
      </p>
      <div class="flex flex-wrap gap-4 mb-10">
        <a href="order.html" class="inline-flex items-center gap-2 bg-forest-600 hover:bg-forest-500 text-white font-bold px-8 py-4 rounded-full shadow-2xl transition-all btn-shine text-base">
          <i class="fa-solid fa-basket-shopping"></i> Place an Order
        </a>
        <a href="about.html" class="inline-flex items-center gap-2 border-2 border-white/50 hover:bg-white hover:text-forest-800 text-white font-bold px-8 py-4 rounded-full transition-all text-base">
          <i class="fa-solid fa-circle-info"></i> Our Story
        </a>
      </div>
      <div class="flex flex-wrap gap-6">
        <div><p class="text-3xl font-black text-white">48<span class="text-brown-200">h</span></p><p class="text-white/60 text-xs uppercase tracking-wider">Fastest delivery</p></div>
        <div class="w-px bg-white/20"></div>
        <div><p class="text-3xl font-black text-white">4,500 <span class="text-brown-200 text-lg">RWF</span></p><p class="text-white/60 text-xs uppercase tracking-wider">Per tray</p></div>
        <div class="w-px bg-white/20"></div>
        <div><p class="text-3xl font-black text-white">100<span class="text-brown-200">%</span></p><p class="text-white/60 text-xs uppercase tracking-wider">Sustainable</p></div>
      </div>
    </div>

    <div data-aos="fade-left" data-aos-duration="900" data-aos-delay="200" class="hidden md:block">
      <div class="glass rounded-3xl p-6 float-anim">
        <img src="eggs.jpg" alt="Fresh Eggs" class="w-full h-56 object-cover rounded-2xl mb-5" />
        <div class="flex items-center justify-between mb-3">
          <div><p class="text-white font-bold text-lg">Fresh Table Eggs</p><p class="text-white/60 text-sm">Tray of 30 eggs</p></div>
          <div class="bg-brown-300 text-gray-900 font-black px-4 py-2 rounded-xl text-sm">4,500 RWF</div>
        </div>
        <div class="grid grid-cols-3 gap-2">
          <div class="bg-white/10 rounded-xl p-2 text-center"><i class="fa-solid fa-seedling text-forest-400 text-lg"></i><p class="text-white text-xs mt-1">Organic</p></div>
          <div class="bg-white/10 rounded-xl p-2 text-center"><i class="fa-solid fa-solar-panel text-brown-200 text-lg"></i><p class="text-white text-xs mt-1">Solar</p></div>
          <div class="bg-white/10 rounded-xl p-2 text-center"><i class="fa-solid fa-truck text-forest-400 text-lg"></i><p class="text-white text-xs mt-1">Fast Delivery</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Highlights strip -->
<div class="bg-gradient-to-r from-forest-800 via-forest-700 to-forest-800 py-10 px-6 md:px-10">
  <div class="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-5 gap-4">
    <div class="flex items-center gap-3 text-white"><div class="w-10 h-10 bg-white/10 rounded-xl flex items-center justify-center shrink-0"><i class="fa-solid fa-egg text-brown-200"></i></div><div><p class="font-bold text-sm">Farm Fresh</p><p class="text-white/60 text-xs">48–72 hr delivery</p></div></div>
    <div class="flex items-center gap-3 text-white"><div class="w-10 h-10 bg-white/10 rounded-xl flex items-center justify-center shrink-0"><i class="fa-solid fa-rotate text-forest-300"></i></div><div><p class="font-bold text-sm">Reliable Supply</p><p class="text-white/60 text-xs">Year-round stock</p></div></div>
    <div class="flex items-center gap-3 text-white"><div class="w-10 h-10 bg-white/10 rounded-xl flex items-center justify-center shrink-0"><i class="fa-solid fa-tag text-brown-200"></i></div><div><p class="font-bold text-sm">Affordable</p><p class="text-white/60 text-xs">Bulk discounts</p></div></div>
    <div class="flex items-center gap-3 text-white"><div class="w-10 h-10 bg-white/10 rounded-xl flex items-center justify-center shrink-0"><i class="fa-solid fa-solar-panel text-brown-200"></i></div><div><p class="font-bold text-sm">Solar + Biogas</p><p class="text-white/60 text-xs">Clean energy</p></div></div>
    <div class="flex items-center gap-3 text-white"><div class="w-10 h-10 bg-white/10 rounded-xl flex items-center justify-center shrink-0"><i class="fa-solid fa-microchip text-forest-300"></i></div><div><p class="font-bold text-sm">Tech-Monitored</p><p class="text-white/60 text-xs">Smart farming</p></div></div>
  </div>
</div>

<!-- Brief intro section -->
<section class="py-20 px-6 md:px-10 bg-white">
  <div class="max-w-4xl mx-auto text-center">
    <span class="inline-block bg-forest-100 text-forest-700 text-xs font-bold px-4 py-1.5 rounded-full uppercase tracking-widest mb-4">Welcome</span>
    <h2 class="font-serif text-3xl md:text-4xl font-black text-gray-900 mb-5">From Our Farm <span class="gradient-text">to Your Table</span></h2>
    <p class="text-gray-600 leading-relaxed mb-8">Eazy Farms is a climate-smart poultry business based in Rwanda, focused on improving access to fresh, affordable eggs using sustainable and technology-driven farming practices.</p>
    <div class="flex flex-wrap justify-center gap-4">
      <a href="about.html" class="inline-flex items-center gap-2 bg-forest-700 hover:bg-forest-600 text-white font-bold px-6 py-3 rounded-full transition-all">Learn More <i class="fa-solid fa-arrow-right"></i></a>
      <a href="products.html" class="inline-flex items-center gap-2 border-2 border-forest-700 text-forest-700 hover:bg-forest-700 hover:text-white font-bold px-6 py-3 rounded-full transition-all">Our Products</a>
    </div>
  </div>
</section>
"""

ABOUT_BODY = page_banner("About Eazy Farms", "Climate-smart poultry farming for a sustainable Rwanda.", "Our Story") + """
<section class="py-24 px-6 md:px-10 bg-forest-50">
  <div class="max-w-7xl mx-auto grid md:grid-cols-2 gap-16 items-center">
    <div class="relative" data-aos="fade-right" data-aos-duration="800">
      <div class="grid grid-cols-2 gap-3">
        <div class="img-overlay rounded-2xl overflow-hidden h-64 col-span-2"><img src="woman-getting-eggs-supermarket.jpg" alt="Eazy Farms" class="w-full h-full object-cover" /></div>
        <div class="img-overlay rounded-2xl overflow-hidden h-40"><img src="eggs.jpg" alt="Fresh eggs" class="w-full h-full object-cover" /></div>
        <div class="img-overlay rounded-2xl overflow-hidden h-40"><img src="hens-factory-chicken-cages.jpg" alt="Farm" class="w-full h-full object-cover" /></div>
      </div>
      <div class="absolute -bottom-4 -right-4 bg-forest-700 text-white rounded-2xl px-5 py-3 shadow-2xl"><p class="text-2xl font-black">100%</p><p class="text-xs text-forest-200">Sustainably Farmed</p></div>
    </div>
    <div data-aos="fade-left" data-aos-duration="800" data-aos-delay="100">
      <span class="inline-block bg-forest-100 text-forest-700 text-xs font-bold px-4 py-1.5 rounded-full uppercase tracking-widest mb-4">About Us</span>
      <h2 class="font-serif text-4xl md:text-5xl font-black text-gray-900 mb-5 leading-tight">Who We <span class="gradient-text">Are</span></h2>
      <p class="text-gray-600 text-base leading-relaxed mb-8">Eazy Farms is a climate-smart poultry business based in Rwanda, focused on improving access to fresh, affordable eggs using sustainable and technology-driven farming practices.</p>
      <div class="space-y-4">
        <div class="bg-white rounded-2xl p-5 shadow-sm border-l-4 border-forest-500 flex gap-4 items-start card-lift">
          <div class="w-10 h-10 bg-forest-100 rounded-xl flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-bullseye text-forest-600"></i></div>
          <div><h4 class="font-bold text-xs uppercase tracking-widest text-forest-600 mb-1">Our Mission</h4><p class="text-gray-700 text-sm leading-relaxed">Provide high-quality, affordable eggs through sustainable practices that benefit our communities and the environment.</p></div>
        </div>
        <div class="bg-white rounded-2xl p-5 shadow-sm border-l-4 border-brown-300 flex gap-4 items-start card-lift">
          <div class="w-10 h-10 bg-brown-50 rounded-xl flex items-center justify-center shrink-0 mt-0.5"><i class="fa-solid fa-eye text-brown-500"></i></div>
          <div><h4 class="font-bold text-xs uppercase tracking-widest text-brown-600 mb-1">Our Vision</h4><p class="text-gray-700 text-sm leading-relaxed">Become a leading provider of sustainably produced eggs in Rwanda, advancing food security for all.</p></div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="py-24 px-6 md:px-10 bg-white relative overflow-hidden">
  <div class="absolute top-0 left-0 w-72 h-72 bg-forest-100 rounded-full blur-3xl opacity-60 -translate-x-1/3 -translate-y-1/3 pointer-events-none"></div>
  <div class="absolute bottom-0 right-0 w-80 h-80 bg-brown-100 rounded-full blur-3xl opacity-50 translate-x-1/3 translate-y-1/3 pointer-events-none"></div>
  <div class="max-w-6xl mx-auto relative">
    <div class="text-center mb-16" data-aos="fade-up">
      <span class="inline-block bg-forest-100 text-forest-700 text-xs font-bold px-4 py-1.5 rounded-full uppercase tracking-widest mb-4">Process</span>
      <h2 class="font-serif text-4xl md:text-5xl font-black text-gray-900 leading-tight mb-4">How It <span class="gradient-text">Works</span></h2>
      <p class="text-gray-500 max-w-lg mx-auto">Four simple steps from our farm to your kitchen.</p>
    </div>
    <div class="grid md:grid-cols-4 gap-6 relative">
      <div class="hidden md:block absolute top-12 left-[12%] right-[12%] h-0.5 bg-gradient-to-r from-forest-200 via-brown-200 to-forest-200 pointer-events-none"></div>
      <div class="text-center relative" data-aos="fade-up"><div class="relative inline-block mb-5"><div class="w-24 h-24 bg-gradient-to-br from-forest-500 to-forest-600 rounded-3xl flex items-center justify-center mx-auto shadow-xl shadow-forest-200 rotate-3"><i class="fa-solid fa-clipboard-list text-white text-3xl"></i></div><div class="absolute -top-2 -right-2 w-8 h-8 bg-white text-forest-700 border-2 border-forest-500 rounded-full flex items-center justify-center font-black text-sm shadow-lg">1</div></div><h3 class="text-gray-900 font-bold text-lg mb-2">Place Order</h3><p class="text-gray-500 text-sm">Fill our simple order form with your details.</p></div>
      <div class="text-center relative" data-aos="fade-up" data-aos-delay="100"><div class="relative inline-block mb-5"><div class="w-24 h-24 bg-gradient-to-br from-brown-300 to-brown-400 rounded-3xl flex items-center justify-center mx-auto shadow-xl shadow-brown-100 -rotate-3"><i class="fa-solid fa-phone text-white text-3xl"></i></div><div class="absolute -top-2 -right-2 w-8 h-8 bg-white text-brown-500 border-2 border-brown-300 rounded-full flex items-center justify-center font-black text-sm shadow-lg">2</div></div><h3 class="text-gray-900 font-bold text-lg mb-2">Confirmation</h3><p class="text-gray-500 text-sm">We call to confirm within 24 hours.</p></div>
      <div class="text-center relative" data-aos="fade-up" data-aos-delay="200"><div class="relative inline-block mb-5"><div class="w-24 h-24 bg-gradient-to-br from-forest-500 to-forest-600 rounded-3xl flex items-center justify-center mx-auto shadow-xl shadow-forest-200 rotate-3"><i class="fa-solid fa-egg text-white text-3xl"></i></div><div class="absolute -top-2 -right-2 w-8 h-8 bg-white text-forest-700 border-2 border-forest-500 rounded-full flex items-center justify-center font-black text-sm shadow-lg">3</div></div><h3 class="text-gray-900 font-bold text-lg mb-2">Fresh Packed</h3><p class="text-gray-500 text-sm">Eggs packed fresh on your delivery day.</p></div>
      <div class="text-center relative" data-aos="fade-up" data-aos-delay="300"><div class="relative inline-block mb-5"><div class="w-24 h-24 bg-gradient-to-br from-brown-300 to-brown-400 rounded-3xl flex items-center justify-center mx-auto shadow-xl shadow-brown-100 -rotate-3"><i class="fa-solid fa-truck text-white text-3xl"></i></div><div class="absolute -top-2 -right-2 w-8 h-8 bg-white text-brown-500 border-2 border-brown-300 rounded-full flex items-center justify-center font-black text-sm shadow-lg">4</div></div><h3 class="text-gray-900 font-bold text-lg mb-2">Delivered</h3><p class="text-gray-500 text-sm">Arrives within 48–72 hours, fresh and ready.</p></div>
    </div>
  </div>
</section>
"""

PRODUCTS_BODY = page_banner("Our Products", "Premium fresh eggs sourced directly from our farm.", "What We Offer") + """
<section class="py-24 px-6 md:px-10 bg-white">
  <div class="max-w-7xl mx-auto">
    <div class="grid md:grid-cols-2 gap-8">
      <div class="bg-gradient-to-br from-forest-50 to-white rounded-3xl overflow-hidden shadow-lg card-lift border border-forest-100" data-aos="fade-up">
        <div class="img-overlay h-60 overflow-hidden"><img src="eggs.jpg" alt="Fresh Table Eggs" class="w-full h-full object-cover" /><div class="absolute bottom-4 left-4 z-10"><span class="bg-forest-600 text-white text-xs font-bold px-3 py-1.5 rounded-full">Best Seller</span></div></div>
        <div class="p-7">
          <div class="flex items-start justify-between mb-3">
            <div><h3 class="text-xl font-black text-gray-900">Fresh Table Eggs</h3><p class="text-gray-500 text-sm">Tray of 30 eggs</p></div>
            <div class="text-right"><p class="text-2xl font-black text-forest-700">4,500</p><p class="text-xs text-gray-400">RWF / tray</p></div>
          </div>
          <p class="text-gray-600 text-sm mb-5 leading-relaxed">Packed fresh and delivered to your door within 48–72 hours of collection. No middleman, no compromise on quality.</p>
          <div class="flex flex-wrap gap-2 mb-5">
            <span class="bg-forest-100 text-forest-700 text-xs font-semibold px-3 py-1 rounded-full"><i class="fa-solid fa-check mr-1"></i>Bulk discounts</span>
            <span class="bg-forest-100 text-forest-700 text-xs font-semibold px-3 py-1 rounded-full"><i class="fa-solid fa-check mr-1"></i>48–72h delivery</span>
            <span class="bg-forest-100 text-forest-700 text-xs font-semibold px-3 py-1 rounded-full"><i class="fa-solid fa-check mr-1"></i>Farm fresh</span>
          </div>
          <a href="order.html" class="block text-center bg-forest-700 hover:bg-forest-600 text-white font-bold py-3 rounded-xl transition-all btn-shine">Order Now <i class="fa-solid fa-arrow-right ml-2"></i></a>
        </div>
      </div>
      <div class="bg-gradient-to-br from-brown-50 to-white rounded-3xl overflow-hidden shadow-lg card-lift border border-brown-100" data-aos="fade-up" data-aos-delay="150">
        <div class="img-overlay h-60 overflow-hidden"><img src="hens-factory-chicken-cages.jpg" alt="Wholesale" class="w-full h-full object-cover" /><div class="absolute bottom-4 left-4 z-10"><span class="bg-brown-500 text-white text-xs font-bold px-3 py-1.5 rounded-full">Wholesale</span></div></div>
        <div class="p-7">
          <div class="flex items-start justify-between mb-3">
            <div><h3 class="text-xl font-black text-gray-900">Bulk / Wholesale</h3><p class="text-gray-500 text-sm">10+ trays</p></div>
            <div class="text-right"><p class="text-2xl font-black text-brown-600">Custom</p><p class="text-xs text-gray-400">pricing</p></div>
          </div>
          <p class="text-gray-600 text-sm mb-5 leading-relaxed">Restaurants, supermarkets, hotels, and schools welcome. Reliable weekly deliveries with volume-based pricing.</p>
          <div class="flex flex-wrap gap-2 mb-5">
            <span class="bg-brown-100 text-brown-700 text-xs font-semibold px-3 py-1 rounded-full"><i class="fa-solid fa-check mr-1"></i>Volume pricing</span>
            <span class="bg-brown-100 text-brown-700 text-xs font-semibold px-3 py-1 rounded-full"><i class="fa-solid fa-check mr-1"></i>Weekly delivery</span>
            <span class="bg-brown-100 text-brown-700 text-xs font-semibold px-3 py-1 rounded-full"><i class="fa-solid fa-check mr-1"></i>Invoicing</span>
          </div>
          <a href="contact.html" class="block text-center bg-brown-500 hover:bg-brown-300 text-white font-bold py-3 rounded-xl transition-all btn-shine">Get a Quote <i class="fa-solid fa-envelope ml-2"></i></a>
        </div>
      </div>
    </div>
  </div>
</section>
"""

DELIVERY_BODY = page_banner("Delivery", "Fast & reliable delivery across Rwanda.", "How We Deliver") + """
<section class="py-24 px-6 md:px-10 bg-gradient-to-b from-white via-brown-50 to-white">
  <div class="max-w-7xl mx-auto">
    <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="bg-forest-50 rounded-2xl p-6 text-center border-t-4 border-forest-500 card-lift" data-aos="fade-up"><div class="w-14 h-14 bg-forest-100 rounded-2xl flex items-center justify-center mx-auto mb-4"><i class="fa-solid fa-city text-forest-600 text-2xl"></i></div><h3 class="font-bold text-gray-900 mb-2">Kigali</h3><p class="text-gray-500 text-sm">Full city coverage, delivered within 48–72 hours.</p></div>
      <div class="bg-forest-50 rounded-2xl p-6 text-center border-t-4 border-forest-500 card-lift" data-aos="fade-up" data-aos-delay="80"><div class="w-14 h-14 bg-forest-100 rounded-2xl flex items-center justify-center mx-auto mb-4"><i class="fa-solid fa-map-location-dot text-forest-600 text-2xl"></i></div><h3 class="font-bold text-gray-900 mb-2">Eastern Province</h3><p class="text-gray-500 text-sm">Serving communities across Eastern Rwanda.</p></div>
      <div class="bg-brown-50 rounded-2xl p-6 text-center border-t-4 border-brown-300 card-lift" data-aos="fade-up" data-aos-delay="160"><div class="w-14 h-14 bg-brown-100 rounded-2xl flex items-center justify-center mx-auto mb-4"><i class="fa-solid fa-clock text-brown-500 text-2xl"></i></div><h3 class="font-bold text-gray-900 mb-2">48–72 Hours</h3><p class="text-gray-500 text-sm">From farm to your door — always fresh.</p></div>
      <div class="bg-brown-50 rounded-2xl p-6 text-center border-t-4 border-brown-300 card-lift" data-aos="fade-up" data-aos-delay="240"><div class="w-14 h-14 bg-brown-100 rounded-2xl flex items-center justify-center mx-auto mb-4"><i class="fa-solid fa-wallet text-brown-500 text-2xl"></i></div><h3 class="font-bold text-gray-900 mb-2">Flexible Payment</h3><p class="text-gray-500 text-sm">Mobile Money, Cash, or Bank Transfer.</p></div>
    </div>

    <div class="mt-16 bg-white rounded-3xl p-8 md:p-12 shadow-xl text-center" data-aos="fade-up">
      <h3 class="font-serif text-2xl md:text-3xl font-black text-gray-900 mb-4">Ready to order?</h3>
      <p class="text-gray-500 mb-6 max-w-md mx-auto">Place your order online and we'll handle the rest. No hidden fees, no delays.</p>
      <a href="order.html" class="inline-flex items-center gap-2 bg-forest-700 hover:bg-forest-600 text-white font-bold px-8 py-3.5 rounded-full transition-all btn-shine"><i class="fa-solid fa-basket-shopping"></i> Place an Order</a>
    </div>
  </div>
</section>
"""

ORDER_BODY = page_banner("Place Your Order", "Fill in the form below and we'll confirm within 24 hours.", "Order Now") + """
<section class="py-20 px-6 md:px-10 bg-gradient-to-br from-forest-50 via-white to-forest-50" x-data="{ orderSuccess: false, orderSubmitting: false, orderError: '' }">
  <div class="max-w-2xl mx-auto">
    <div class="bg-white rounded-3xl shadow-2xl overflow-hidden" data-aos="fade-up">
      <form id="orderForm" class="p-8 md:p-10" x-show="!orderSuccess"
            @submit.prevent="
              orderSubmitting = true; orderError = '';
              fetch('https://formsubmit.co/ajax/akotonimohchristine@gmail.com', {
                method:'POST', headers:{'Content-Type':'application/json','Accept':'application/json'},
                body: JSON.stringify(Object.fromEntries(new FormData($event.target)))
              }).then(r=>r.json()).then(d=>{ orderSubmitting=false; orderSuccess=true; $event.target.reset(); })
              .catch(e=>{ orderSubmitting=false; orderError='Could not send order. Please call us at +250 798 287 234.'; });">
        <input type="hidden" name="_subject" value="New Order from EazyFarms Website" />
        <input type="hidden" name="_template" value="table" />
        <input type="hidden" name="_captcha" value="false" />
        <input type="hidden" name="_cc" value="gbagidiezekiel@gmail.com" />
        <input type="text" name="_honey" style="display:none" />

        <div class="grid md:grid-cols-2 gap-5">
          <div class="flex flex-col gap-1.5"><label class="text-sm font-semibold text-gray-700" for="name"><i class="fa-solid fa-user text-forest-500 mr-1.5"></i>Full Name</label><input type="text" id="name" name="Full Name" placeholder="Your full name" required class="form-input w-full px-4 py-3 border-2 border-gray-200 rounded-xl text-sm" /></div>
          <div class="flex flex-col gap-1.5"><label class="text-sm font-semibold text-gray-700" for="phone"><i class="fa-solid fa-phone text-forest-500 mr-1.5"></i>Phone Number</label><input type="tel" id="phone" name="Phone" placeholder="+250 7XX XXX XXX" required class="form-input w-full px-4 py-3 border-2 border-gray-200 rounded-xl text-sm" /></div>
          <div class="flex flex-col gap-1.5 md:col-span-2"><label class="text-sm font-semibold text-gray-700" for="location"><i class="fa-solid fa-location-dot text-forest-500 mr-1.5"></i>Delivery Location</label><input type="text" id="location" name="Delivery Location" placeholder="District, sector or street address" required class="form-input w-full px-4 py-3 border-2 border-gray-200 rounded-xl text-sm" /></div>
          <div class="flex flex-col gap-1.5"><label class="text-sm font-semibold text-gray-700" for="quantity"><i class="fa-solid fa-boxes-stacked text-forest-500 mr-1.5"></i>Number of Trays</label><input type="number" id="quantity" name="Trays" min="1" placeholder="e.g. 5" required class="form-input w-full px-4 py-3 border-2 border-gray-200 rounded-xl text-sm" /></div>
          <div class="flex flex-col gap-1.5"><label class="text-sm font-semibold text-gray-700" for="date"><i class="fa-solid fa-calendar text-forest-500 mr-1.5"></i>Preferred Delivery Date</label><input type="date" id="date" name="Delivery Date" required class="form-input w-full px-4 py-3 border-2 border-gray-200 rounded-xl text-sm" /></div>
          <div class="flex flex-col gap-1.5 md:col-span-2">
            <label class="text-sm font-semibold text-gray-700"><i class="fa-solid fa-credit-card text-forest-500 mr-1.5"></i>Payment Method</label>
            <div class="grid grid-cols-3 gap-3">
              <label class="pay-card"><input type="radio" name="Payment Method" value="Mobile Money" class="hidden" checked /><div class="pay-inner text-sm"><i class="fa-solid fa-mobile-screen-button text-forest-500"></i> Mobile Money</div></label>
              <label class="pay-card"><input type="radio" name="Payment Method" value="Cash on Delivery" class="hidden" /><div class="pay-inner text-sm"><i class="fa-solid fa-money-bill text-forest-500"></i> Cash on Delivery</div></label>
              <label class="pay-card"><input type="radio" name="Payment Method" value="Bank Transfer" class="hidden" /><div class="pay-inner text-sm"><i class="fa-solid fa-building-columns text-forest-500"></i> Bank Transfer</div></label>
            </div>
          </div>
          <div class="flex flex-col gap-1.5 md:col-span-2"><label class="text-sm font-semibold text-gray-700" for="notes"><i class="fa-solid fa-note-sticky text-forest-500 mr-1.5"></i>Additional Notes <span class="text-gray-400 font-normal">(optional)</span></label><textarea id="notes" name="Notes" rows="3" placeholder="Any special instructions…" class="form-input w-full px-4 py-3 border-2 border-gray-200 rounded-xl text-sm resize-none"></textarea></div>
        </div>

        <div x-show="orderError" x-cloak class="mt-5 p-4 bg-red-50 border border-red-200 rounded-xl text-red-700 text-sm"><i class="fa-solid fa-circle-exclamation mr-1"></i> <span x-text="orderError"></span></div>

        <button type="submit" :disabled="orderSubmitting" class="mt-7 w-full bg-forest-700 hover:bg-forest-600 disabled:opacity-60 text-white font-bold py-4 rounded-2xl transition-all btn-shine text-base shadow-lg shadow-forest-700/30">
          <span x-show="!orderSubmitting"><i class="fa-solid fa-paper-plane mr-2"></i> Submit Order</span>
          <span x-show="orderSubmitting" x-cloak><i class="fa-solid fa-spinner fa-spin mr-2"></i> Sending…</span>
        </button>
        <p class="text-center text-xs text-gray-400 mt-4"><i class="fa-solid fa-shield-halved text-forest-400 mr-1"></i> Your information is secure and will only be used to process your order.</p>
      </form>

      <div x-show="orderSuccess" x-cloak x-transition class="p-12 text-center">
        <div class="w-20 h-20 bg-forest-100 rounded-full flex items-center justify-center mx-auto mb-5"><i class="fa-solid fa-circle-check text-forest-600 text-4xl"></i></div>
        <h3 class="text-2xl font-black text-gray-900 mb-2">Order Received!</h3>
        <p class="text-gray-500 mb-6">Thank you! We'll contact you within 24 hours to confirm your delivery details.</p>
        <button @click="orderSuccess = false; document.getElementById('orderForm').reset()" class="bg-forest-700 text-white font-bold px-8 py-3 rounded-xl hover:bg-forest-600 transition-all">Place Another Order</button>
      </div>
    </div>
  </div>
</section>
"""

CONTACT_BODY = page_banner("Get In Touch", "Questions, bulk orders, or partnerships? We'd love to hear from you.", "Contact Us") + """
<section class="py-20 px-6 md:px-10 bg-gradient-to-b from-white via-brown-50 to-white relative overflow-hidden">
  <div class="absolute top-20 right-10 w-64 h-64 bg-forest-100 rounded-full blur-3xl opacity-50 pointer-events-none"></div>
  <div class="absolute bottom-20 left-10 w-56 h-56 bg-brown-200 rounded-full blur-3xl opacity-40 pointer-events-none"></div>
  <div class="max-w-5xl mx-auto relative">
    <div class="grid md:grid-cols-3 gap-6">
      <a href="tel:+250798287234" class="group bg-white rounded-3xl p-8 text-center shadow-lg card-lift border border-gray-100 block" data-aos="fade-up">
        <div class="w-16 h-16 bg-gradient-to-br from-forest-500 to-forest-600 rounded-2xl flex items-center justify-center mx-auto mb-5 shadow-lg shadow-forest-200 group-hover:scale-110 transition-transform"><i class="fa-solid fa-phone text-white text-2xl"></i></div>
        <h4 class="text-forest-700 text-xs uppercase tracking-widest mb-2 font-bold">Phone</h4>
        <p class="text-gray-900 font-bold text-base mb-1">+250 798 287 234</p>
        <span class="inline-flex items-center gap-1 text-forest-600 text-xs font-semibold mt-2">Call us <i class="fa-solid fa-arrow-right group-hover:translate-x-1 transition-transform"></i></span>
      </a>
      <a href="mailto:akotonimohchristine@gmail.com" class="group bg-white rounded-3xl p-8 text-center shadow-lg card-lift border border-gray-100 block" data-aos="fade-up" data-aos-delay="100">
        <div class="w-16 h-16 bg-gradient-to-br from-brown-300 to-brown-400 rounded-2xl flex items-center justify-center mx-auto mb-5 shadow-lg shadow-brown-100 group-hover:scale-110 transition-transform"><i class="fa-solid fa-envelope text-white text-2xl"></i></div>
        <h4 class="text-brown-500 text-xs uppercase tracking-widest mb-2 font-bold">Email</h4>
        <p class="text-gray-900 font-bold text-base mb-1 break-all">akotonimohchristine@gmail.com</p>
        <span class="inline-flex items-center gap-1 text-brown-500 text-xs font-semibold mt-2">Send email <i class="fa-solid fa-arrow-right group-hover:translate-x-1 transition-transform"></i></span>
      </a>
      <div class="bg-white rounded-3xl p-8 text-center shadow-lg card-lift border border-gray-100" data-aos="fade-up" data-aos-delay="200">
        <div class="w-16 h-16 bg-gradient-to-br from-forest-500 to-forest-600 rounded-2xl flex items-center justify-center mx-auto mb-5 shadow-lg shadow-forest-200"><i class="fa-solid fa-location-dot text-white text-2xl"></i></div>
        <h4 class="text-forest-700 text-xs uppercase tracking-widest mb-2 font-bold">Location</h4>
        <p class="text-gray-900 font-bold text-base mb-1">Eastern Province</p>
        <p class="text-gray-500 text-sm">Rwanda</p>
      </div>
    </div>
    <div class="mt-12 bg-gradient-to-r from-forest-600 to-forest-700 rounded-3xl p-8 md:p-10 text-center shadow-2xl shadow-forest-200" data-aos="fade-up">
      <h3 class="text-white font-serif text-2xl md:text-3xl font-black mb-3">Ready to taste the difference?</h3>
      <p class="text-forest-100 mb-6 max-w-md mx-auto">Place your first order today and get fresh eggs delivered within 48–72 hours.</p>
      <a href="order.html" class="inline-flex items-center gap-2 bg-white text-forest-700 font-bold px-8 py-3.5 rounded-full hover:bg-brown-50 transition-all shadow-lg"><i class="fa-solid fa-basket-shopping"></i> Order Now</a>
    </div>
  </div>
</section>
"""

# ============ BUILD ============
PAGES = [
    ("index.html",    "home",     "Eazy Farms – Fresh. Reliable. Sustainable.", HOME_BODY),
    ("about.html",    "about",    "About – Eazy Farms",                          ABOUT_BODY),
    ("products.html", "products", "Products – Eazy Farms",                       PRODUCTS_BODY),
    ("delivery.html", "delivery", "Delivery – Eazy Farms",                       DELIVERY_BODY),
    ("order.html",    "order",    "Place an Order – Eazy Farms",                 ORDER_BODY),
    ("contact.html",  "contact",  "Contact – Eazy Farms",                        CONTACT_BODY),
]

import os
out_dir = os.path.dirname(os.path.abspath(__file__))
for filename, active, title, body in PAGES:
    html = HEAD.replace("__TITLE__", title) + nav(active) + body + FOOTER
    with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  built {filename}")

print("\nDone — multi-page site generated.")
