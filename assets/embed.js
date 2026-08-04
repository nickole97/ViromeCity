<script>
// The interactive figures are their own pages — their CSS is global (body, h1,
// :root), so inlining one into a chapter would restyle the chapter. An iframe
// keeps them isolated and still shows them in the reading flow.
//
// The cost of an iframe is that it has no natural height. Each widget measures
// itself and posts it here; see the script at the foot of components/*.html.
(function () {
  var MIN = 320;

  window.addEventListener('message', function (e) {
    var d = e.data;
    if (!d || d.viromeEmbed !== true || typeof d.height !== 'number') return;

    document.querySelectorAll('.embed iframe').forEach(function (f) {
      // Match on the path the widget reported, so two embeds on one page do
      // not resize each other.
      if (f.contentWindow !== e.source) return;
      f.style.height = Math.max(MIN, d.height) + 'px';
    });
  });
})();
</script>
