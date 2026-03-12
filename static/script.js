document.addEventListener("DOMContentLoaded", function () {
	const revealItems = document.querySelectorAll(".reveal-up");
	const navbar = document.querySelector(".academy-navbar");

	if ("IntersectionObserver" in window) {
		const observer = new IntersectionObserver(
			function (entries) {
				entries.forEach(function (entry) {
					if (entry.isIntersecting) {
						entry.target.classList.add("is-visible");
						observer.unobserve(entry.target);
					}
				});
			},
			{ threshold: 0.15 }
		);

		revealItems.forEach(function (item) {
			observer.observe(item);
		});
	} else {
		revealItems.forEach(function (item) {
			item.classList.add("is-visible");
		});
	}

	function updateNavbarState() {
		if (!navbar) {
			return;
		}

		if (window.scrollY > 20) {
			navbar.classList.add("is-scrolled");
		} else {
			navbar.classList.remove("is-scrolled");
		}
	}

	updateNavbarState();
	window.addEventListener("scroll", updateNavbarState, { passive: true });
});