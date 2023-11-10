<template>
    <body class="body">
        <iframe :src="url" width="1200vh" height="800px" frameborder="0"></iframe>
    </body>
</template>
<script>
export default {

    data(){
        return {
            url: `http://${process.env.VUE_APP_USER_IP_WITHPORT}/static/Annotate.html`

        }
    }
}
</script>

<style scoped src="./Annotate.css"></style>