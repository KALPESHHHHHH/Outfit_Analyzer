document.addEventListener('DOMContentLoaded', function() {
    // Get all toggle elements
    const sidebarContainer = document.querySelector('.sidebar-container');
    const sidebarToggle = document.getElementById('sidebarToggle');
    const closeSidebar = document.getElementById('closeSidebar');

    // Function to toggle sidebar
    function toggleSidebar() {
        sidebarContainer.classList.toggle('show');

        // Toggle aria-expanded for accessibility
        const isExpanded = sidebarContainer.classList.contains('show');
        if (sidebarToggle) sidebarToggle.setAttribute('aria-expanded', isExpanded);
    }

    // Function to close sidebar
    function closeSidebarFunc() {
        sidebarContainer.classList.remove('show');
        if (sidebarToggle) sidebarToggle.setAttribute('aria-expanded', 'false');
    }

    // Add event listeners to all toggle buttons
    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', toggleSidebar);
        sidebarToggle.setAttribute('aria-label', 'Toggle sidebar navigation');
        sidebarToggle.setAttribute('aria-controls', 'sidebar');
    }

    if (closeSidebar) {
        closeSidebar.addEventListener('click', closeSidebarFunc);
        closeSidebar.setAttribute('aria-label', 'Close sidebar navigation');
    }

    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', function(event) {
        const isClickInsideSidebar = sidebarContainer.contains(event.target);
        const isClickOnToggle = sidebarToggle && sidebarToggle.contains(event.target);

        if (!isClickInsideSidebar && !isClickOnToggle && window.innerWidth < 992) {
            closeSidebarFunc();
        }
    });

    // Handle window resize
    function handleResize() {
        if (window.innerWidth >= 992) {
            // Always show sidebar on desktop
            sidebarContainer.classList.add('show');
        } else {
            // Hide sidebar by default on mobile
            sidebarContainer.classList.remove('show');
        }

        // Update aria-expanded state
        const isExpanded = sidebarContainer.classList.contains('show');
        if (sidebarToggle) sidebarToggle.setAttribute('aria-expanded', isExpanded);
    }

    // Initial setup
    handleResize();

    // Add resize event listener with debounce
    let resizeTimer;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(handleResize, 250);
    });

    // Add keyboard accessibility
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape' && window.innerWidth < 992) {
            closeSidebarFunc();
        }
    });
});
