<template>
  <body class="body">
    <div class="container" id="container">
        <div class="left">
            <form  class="form" action="">
                <label for="images">Images:</label>
                <input type="file" id="images" name="images[]" accept="image/jpeg, image/png" multiple />
                <input type="button" name="cropImages" id="cropImages" value="Crop&Save" />

                <br />

                <label for="imageSearch">Search:</label>
                <input type="text" id="imageSearch" name="imageSearch" />

                <label for="imageList"></label><select name="imageList" id="imageList" size="10" multiple></select>

                <div id="imageInformation"></div>
                <hr class="hr"/>

                <label for="classes">Classes:</label>
                <input type="file" id="classes" name="classes" accept="text/plain" />
                <label for="classList"></label><select name="classList" id="classList" size="10" multiple></select>

                <div id="bboxInformation"></div>
                <hr class="hr"/>

                <label for="bboxes">Bboxes:</label>
                <input type="file" id="bboxes" name="bboxes[]" accept="text/plain, application/zip" disabled multiple />
                <input type="button" name="restoreBboxes" id="restoreBboxes" value="Restore" disabled />
                <input type="button" name="saveBboxes" id="saveBboxes" value="Save YOLO" />

                <div id="voc">
                    <label for="vocFolder">Voc folder:</label>
                    <input type="text" id="vocFolder" name="vocFolder" value="data" />
                    <input type="button" name="saveVocBboxes" id="saveVocBboxes" value="Save VOC" />
                    <input type="button" name="saveCocoBboxes" id="saveCocoBboxes" value="Save COCO" />
                </div>
                <div id="coco">

                </div>
                <hr class="hr"/>

                <div id="description">
                    SHORTCUTS:
                    <ul>
                        <li>
                            Mouse WHEEL - zoom in/out image
                        </li>
                        <li>
                            Mouse RIGHT BUTTON - pan image
                        </li>
                        <li>
                            Arrows LEFT and RIGHT - cycle images
                        </li>
                        <li>
                            Arrows Up and DOWN - cycle classes
                        </li>
                        <li>
                            Key DELETE - remove selected Bbox
                        </li>
                    </ul>

                    <p>Version: 0.2.4 | Copyright © 2018-2019 Draining Sun.</p>
                </div>
            </form>
        </div>

        <div class="right" id="right">
            <canvas id="canvas"></canvas>
            <canvas id="hiddenCanvas"></canvas>
        </div>
    </div>
</body>
</template>

<script>
export default {

}
</script>

<style>
.body {
    overflow: hidden;
}

.form {
    height: 100%
}

hr {
    width: 100%;
}

.container {
    display: block;
    position: absolute;
    height: auto;
    bottom: 0;
    top: 0;
    left: 0;
    right: 0;
}

.column_wrap {
    position: relative;
}

.left {
    width: calc(30% - 10px);
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    height: auto;
    display: block;
    margin: 10px 0 10px 10px;
}

.right {
    border-left: 1px solid gray;
    margin: 10px 10px 10px calc(30% + 10px);
    padding-left: 10px;
}

#images, #classes, #bboxes {
    width: 175px;
    margin-top: 10px;
}

#bboxes {
    width: 130px;
}

#imageList, #classList, #description {
    width: 100%;
    margin-top: 10px;
    margin-bottom: 10px;
    height: 18%;
}

#saveClasses, #saveBboxes, #saveVocBboxes, #saveCocoBboxes, #restoreBboxes, #cropImages {
    float: right;
    margin-left: 10px;
    margin-top: 10px;
    margin-bottom: 10px;
}

#imageSearch {
    margin-top: 10px;
}

#imageInformation, #bboxInformation {
    height: 20px;
    width: 100%;
}

#voc {
    margin-top: 10px;
}

#vocFolder {
    width: 95px;
}

#saveVocBboxes, #saveCocoBboxes {
    margin-top: 0;
    margin-bottom: 0;
}

</style>