<script type="text/javascript">
	(function setSelected(elementId) {
		var div = document.getElementById(elementId);
		div.className = 'selected ' + div.className
	})('{{ elementId }}');
</script>