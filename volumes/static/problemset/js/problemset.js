function toggleFilterSection() {
    var filterSection = document.getElementById('filterSection');
    filterSection.style.display = (filterSection.style.display === 'none' || filterSection.style.display === '') ? 'block' : 'none';
    document.getElementById('close-filter-section').style.display = 'block';
}

function closeFilterSection() {
    var filterSection = document.getElementById('filterSection');
    filterSection.style.display = (filterSection.style.display === 'none' || filterSection.style.display === '') ? 'block' : 'none';
}