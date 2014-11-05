from StringIO import StringIO
import xhtml2pdf.pisa as pisa

html_data = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>PDF Title</title>
        <meta name="author" content="this appears in the author metadata of the PDF">
        <style type="text/css">
            @page { /* size and margin of resulting PDF pages */
                size: letter;
                margin: 2cm;
            }

            @font-face {
                font-family: Noto;
                src: url('noto.ttf');
            }
            @font-face {
                font-family: Noto;
                src: url('noto-bold.ttf');
                font-weight: bold;
            }
            @font-face {
                font-family: Noto;
                src: url('noto-italic.ttf');
                font-style: italic;
            }
            @font-face {
                font-family: Noto;
                src: url('noto-bold-italic.ttf');
                font-weight: bold;
                font-style: italic;
            }

            body {
                background-color: white;
                color: black;
                font-size: 14px;
                font-family: Noto;
            }

            .main-title {
                font-size: 50px;
                margin-bottom: 20px;
                font-weith: bold;
            }

            .example {
                margin-bottom: 15px;
            }

            .border-example {
                border-bottom-color: #5677fc;
                border-bottom-style: double;
                border-bottom-width: 1;
                border-left-color: #e84e40;
                border-left-style: dotted;
                border-left-width: 2;
                border-right-color: #e84e40;
                border-right-style: solid;
                border-right-width: 3;
                border-top-color: #5677fc;
                border-top-style: dashed;
                border-top-width: 4;
            }
        </style>
    </head>
    <body>
        <div class="main-title">Demo xhtml2pdf</div>

        <h1>Table</h1>

        <h3>Basic table (background-color: #CCC)</h3>
        <table style="background-color: #CCC">
            <tr>
                <td>Test</td>
                <td>Test 2</td>
            </tr>
        </table>

        <h3>Table with colspan</h3>
        <table style="background-color: #CCC">
            <tr>
                <th colspan="4" style="background-color: #5677fc; color: white;">
                    Bloc 1
                </th>
                <th colspan="4" style="background-color: #e84e40; color: white;">
                    Bloc 2
                </th>
                <th colspan="4" style="background-color: #ffeb3b">
                    Bloc 3
                </th>
            </tr>
            <tr>
                <th colspan="6" style="background-color: #ffeb3b">
                    Bloc 4
                </th>
                <th colspan="6" style="background-color: #7e57c2; color: white;">
                    Bloc 5
                </th>
            </tr>
            <tr>
                <th colspan="3" style="background-color: #5677fc; color: white;">
                    Bloc 6
                </th>
                <th colspan="3" style="background-color: #e84e40; color: white;">
                    Bloc 7
                </th>
                <th colspan="3" style="background-color: #5677fc; color: white;">
                    Bloc 8
                </th>
                <th colspan="3" style="background-color: #ffeb3b">
                    Bloc 9
                </th>
            </tr>
        </table>

        <h3>Table with specific percentage width</h3>
        <table style="background-color: #CCC;">
            <tr>
                <td style="background-color: #5677fc; color: white; width: 50%;">
                    Bloc 1: 50%
                </td>
                <td style="background-color: #e84e40; color: white; width: 20%;">
                    Bloc 2: 20%
                </td>
                <td style="background-color: #ffeb3b">
                    Bloc 3: auto
                </td>
            </tr>
        </table>
        <table style="background-color: #CCC;">
            <tr>
                <td style="background-color: #5677fc; color: white; width: 50%;">
                    Bloc 1: 50%
                </td>
                <td style="background-color: #e84e40; color: white; width: 20%;">
                    Bloc 2: 20%
                </td>
                <td style="background-color: #ffeb3b; width: 30%;">
                    Bloc 3: 30%
                </td>
            </tr>
        </table>

        <h3>Table with specific px width</h3>
        <table style="background-color: #CCC;">
            <tr>
                <td colspan="6" style="background-color: #ffeb3b; width: 200px;">
                    Bloc 4 200px (not working)
                </td>
                <td colspan="6" style="background-color: #7e57c2; color: white;">
                    Bloc 5 auto
                </td>
            </tr>
        </table>
        <table style="background-color: #CCC;">
            <tr>
                <td colspan="6" style="background-color: #ffeb3b; width: 200px;">
                    Bloc 4 200px (not working)
                </td>
                <td colspan="6" style="background-color: #7e57c2; color: white; width: 300px;">
                    Bloc 5 300px
                </td>
            </tr>
        </table>

        <h3>Table with headers</h3>
        <table style="background-color: #CCC">
            <tr>
                <th>Test</th>
                <th>Test 2</th>
            </tr>
            <tr>
                <td>Test</td>
                <td>Test 2</td>
            </tr>
        </table>

        <h3>Table with headers repeated on every pages</h3>
        <table style="background-color: #CCC" repeat="1">
            <tr>
                <th>Test</th>
                <th>Test 2</th>
            </tr>
            <tr>
                <td>Test</td>
                <td>Test 2</td>
            </tr>
            <tr>
                <td>Test</td>
                <td>Test 2</td>
            </tr>
            <tr>
                <td>Test</td>
                <td>Test 2</td>
            </tr>
            <tr>
                <td>Test</td>
                <td>Test 2</td>
            </tr>
            <tr>
                <td>Test</td>
                <td>Test 2</td>
            </tr>
            <tr>
                <td>Test</td>
                <td>Test 2</td>
            </tr>
            <tr>
                <td>Test</td>
                <td>Test 2</td>
            </tr>
            <tr>
                <td>Test</td>
                <td>Test 2</td>
            </tr>
            <tr>
                <td>Test</td>
                <td>Test 2</td>
            </tr>
        </table>

        <h1>Image</h1>
        <img src="test.jpg" />

        <h1>List</h1>
        <ul>
            <li>Test</li>
            <li>Test 2</li>
        </ul>

        <h1>Ordered list</h1>
        <ol>
            <li>Test</li>
            <li>Test 2</li>
        </ol>

        <h1>Styling</h1>
        <div>
            <div class="example" style="background-color: #CCC">background-color</div>
            <div class="example" style="border: 2px solid #CCC">Simple border</div>
            <div class="example border-example">Full border (dashed, dotted, solid, double)</div>
            <div class="example" style="color: #5677fc;">Color</div>
            <div class="example"
                <div style="background-color: #CCC; display: block;">Block</div>
            </div>
            <div class="example">
                <div style="background-color: #CCC; display: inline;">inline</div>
            </div>
            <div class="example">
                <div style="background-color: #CCC; display: inline-block; width: 500px;">inline-block (wdith not working)</div>
            </div>
            <div class="example" style="font-family: Serif; font-size: 20px; font-style: italic; font-weight: bold;">Font</div>
            <div class="example" style="background-color: #CCC; height: 200px;">Height 200px</div>
            <div class="example" style="background-color: #CCC; line-height: 100px;">Line-height 100px</div>
            <div class="example">
                List type square:
                <ul style="list-style-type: square; font-size: 25px;">
                    <li>Test</li>
                    <li>Test 2</li>
                </ul>
            </div>
            <div class="example" style="background-color: #CCC; margin: 50px;">Margin 50px</div>
            <div class="example" style="background-color: #CCC; padding: 50px;">Padding 50px</div>
            <div class="example" style="text-align: right;">Text align right</div>
            <div class="example" style="text-decoration: underline;">Text decoration underline</div>
            <div class="example" style="text-indent: 50px;">Text indent 50px</div>
            <div class="example" style="background-color: #CCC; line-height: 50px; vertical-align: bottom;">Vertical align bottom</div>
            <div class="example" style="background-color: #CCC; width: 200px;">Width 200px</div>
            <div class="example" style="background-color: #CCC; width: 50%;">Width 50%</div>
        </div>


        <h1>Table of Contents</h1>
        <pdf:toc />
    </body>
</html>
"""
html_data = html_data.encode('utf8')
html_data = StringIO(html_data)

output = StringIO()
pisa.log.setLevel('WARNING') #suppress debug log output
pdf = pisa.CreatePDF(
    html_data,
    output,
    encoding='utf-8',
)

pdf_data = pdf.dest.getvalue()
with open('out.pdf', 'w+') as f:
    f.write(pdf_data)