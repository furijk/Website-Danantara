// Call the dataTables jQuery plugin
$(document).ready(function() {
  // initialize DataTable with ordering disabled so it preserves row order from uploads
  // but only if it hasn't been initialised already (prevents reinitialisation warning)
  if (!$.fn.DataTable.isDataTable('#dataTable')) {
    $('#dataTable').DataTable({ ordering: false });
  }
});
