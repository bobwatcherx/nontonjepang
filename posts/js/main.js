 // Function to get URL parameters
        function getParameterByName(name, url) {
            if (!url) url = window.location.href;
            name = name.replace(/[\[\]]/g, "\\$&");
            var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
                results = regex.exec(url);
            if (!results) return null;
            if (!results[2]) return '';
            return decodeURIComponent(results[2].replace(/\+/g, " "));
        }

        // Update image src based on URL parameter 'image'
        var imageUrl = getParameterByName('image') || '';
        document.querySelector('img').src = "https://bobwatcherx.github.io/nontonjepang/image/" + imageUrl;

        // Update link href based on URL parameter 'id'
        var videoId = getParameterByName('id') || 'defaultVideoId';
        document.querySelector('a').href = "nonton/index.html?id=" + videoId;

        // Fetch and insert content from iklan.html
        fetch('iklan.html')
            .then(response => response.text())
            .then(data => {
                document.getElementById('iklanContainer').innerHTML = data;
            })
            .catch(error => console.error('Error fetching iklan.html:', error));