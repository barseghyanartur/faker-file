/**
 * Sphinx `:download:` directive integration with PrismJS.
 *
 * Install the snippet by adding it to the sphinx conf.py configuration
 * as shown below:
 *
 *   prismjs_base = "//cdnjs.cloudflare.com/ajax/libs/prism/1.29.0"
 *
 *   html_css_files = [
 *       f"{prismjs_base}/themes/prism.min.css",
 *       f"{prismjs_base}/plugins/toolbar/prism-toolbar.min.css",
 *       f"{prismjs_base}/plugins/copy-to-clipboard/prism-copy-to-clipboard.min.css",
 *       "css/prism_sphinx_rtd_theme.css",
 *   ]
 *
 *   html_js_files = [
 *       f"{prismjs_base}/prism.min.js",
 *       f"{prismjs_base}/plugins/autoloader/prism-autoloader.min.js",
 *       f"{prismjs_base}/plugins/toolbar/prism-toolbar.min.js",
 *       f"{prismjs_base}/plugins/copy-to-clipboard/prism-copy-to-clipboard.min.js",
 *       "js/inline_code.js",
 *   ]
 *
 * @author Artur Barseghyan (https://github.com/barseghyanartur)
 * @version 1.0
 */

$(document).ready(function() {
    // Find all download links by their class
    $("a.reference.download.internal").each(function(index) {
        // Create a unique id for the additional content div
        let contentID = 'additional-content-' + index;

        // Get the file extension and set language class
        let fileExtension = $(this).attr('href').split('.').pop();
        let langClass = fileExtension === 'py' ? 'language-python' :
                        fileExtension === 'js' ? 'language-javascript' :
                        'language-plaintext';

        // Append a new div for the additional content after the link
        $(this).after(
            `<div id="${contentID}" style="display:none;"><pre><code class="${langClass}"></code></pre></div>`
        );

        // Attach a click event to the download link
        $(this).on('click', function(event) {
            event.preventDefault(); // Stop the link from being followed
            let additionalContentDiv = $(`#${contentID}`);
            let additionalContent = $(`#${contentID} code`);

            if (additionalContentDiv.is(":visible")) {
                additionalContentDiv.hide();
            } else {
                // Check if content has been fetched
                if (!additionalContentDiv.hasClass('fetched')) {
                    let retries = 3;
                    let url = $(this).attr('href');
                    function fetchContent() {
                        // Fetch the content of the file and display it
                        $.ajax({
                            url: url,
                            dataType: 'text',
                            success: function (data) {
                                additionalContent.text(data);
                                Prism.highlightElement(additionalContent[0]);
                                additionalContentDiv.show();
                                // Add fetched class
                                additionalContentDiv.addClass('fetched');
                            },
                            error: function () {
                                additionalContent.text('Error fetching content.');
                                additionalContentDiv.show();
                            }
                        });
                    }
                    fetchContent();
                } else {
                    // Content has been fetched, just show it
                    additionalContentDiv.show();
                }
            }
        });
    });
});
