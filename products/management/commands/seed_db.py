from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Seeds the database with initial products'

    def handle(self, *args, **kwargs):
        products = [
            ("Wireless Mechanical Keyboard V2", "A high-performance compact 75% mechanical keyboard with factory-lubed linear switches, hot-swappable PCB, customizable per-key RGB lighting, and an impressive 3-month battery life. Perfect for both deep programming sessions and high-tier competitive gaming."),
            ("Pro USB-C 8-in-1 Hub", "A premium aluminum docking solution that instantly expands a single USB-C port to include 4K@60Hz HDMI output, Gigabit Ethernet, 100W Power Delivery passthrough, SD/TF card readers, and dual USB-A 3.2 Gen 2 ports delivering 10Gbps data transfer speeds."),
            ("Studio Noise Cancelling Headphones", "Industry-leading over-ear acoustic headphones engineered with dual noise sensor technology. Experience rich, high-fidelity audio with deep bass profiles. Includes multipoint Bluetooth 5.3 pairing, a plush memory-foam headband, and up to 45 hours of uninterrupted playback."),
            ("Armor Portable SSD 2TB", "Ultra-rugged, IP68 water and dust-resistant portable solid-state drive built for creators on the move. Features explosive read/write speeds up to 2000MB/s via USB 3.2 Gen 2x2. Comes protected in a shock-absorbent silicone bumper case."),
            ("Zenith Ergonomic Vertical Mouse", "Scientifically designed vertical mouse to reduce wrist strain and prevent carpal tunnel syndrome. Equipped with a high-precision 4000 DPI optical sensor, whisper-quiet tactile clicks, a dedicated thumb rest, and 6 programmable side buttons."),
            ("UltraVision 4K Pro Webcam", "Broadcast-grade 4K HDR webcam delivering razor-sharp video quality even in low-light environments. Built-in AI auto-framing, dual noise-reducing stereo microphones, 90-degree wide field of view, and an integrated physical privacy shutter for complete security."),
            ("Cloud Step Standing Desk Mat", "Premium 1-inch thick anti-fatigue floor mat designed with a solid high-density polyurethane foam core. Significantly reduces lower back and leg pressure during extended standing sessions. Features a puncture-proof synthetic leather top and non-slip bottom grip."),
            ("Aero Dual Monitor Desk Mount", "Heavy-duty articulating gas spring monitor arm built from aerospace-grade aluminum. Effortlessly supports two 32-inch displays up to 20lbs each. Features 360-degree rotation, integrated cable management channels, and a quick-release VESA plate."),
            ("Lumina Smart LED Desk Lamp", "A minimalist, clamp-on LED task lamp delivering soft, flicker-free illumination over your entire workspace. Smart touch controls allow adjustment between 5 color temperatures and infinite brightness levels. Features an ambient back-glow mode and a fast-charging USB-C port."),
            ("Titan Aluminum Folding Laptop Stand", "A portable, ventilating laptop elevator crafted from a single seamless block of anodized aluminum. Fully adjustable up to 8 different viewing angles to correct posture. Silicone anti-slip pads secure laptops ranging from 10 to 17 inches safely in place."),
        ]
        
        count = 0
        for name, desc in products:
            obj, created = Product.objects.get_or_create(
                name=name, 
                defaults={'description': desc}
            )
            if created:
                count += 1
                
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {count} new product(s) to the DB. Skip existing ones.'))
