<template>
  <div style="background-color: rgb(248,248,248);font-family: Rubik, sans-serif;">
        <nav class="navbar navbar-light navbar-expand-md shadow navigation-clean">
            <div class="container"><a class="navbar-brand" href="#">SocGen Matching</a><button class="navbar-toggler" data-toggle="collapse" data-target="#navcol-1"><span class="sr-only">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
                <div class="collapse navbar-collapse"
                    id="navcol-1">
                    <ul class="nav navbar-nav ml-auto">
                        <li class="nav-item" role="presentation"><nuxt-link class="nav-link" to="/">One-to-One</nuxt-link></li>
                        <li class="nav-item" role="presentation"><nuxt-link class="nav-link" to="/manytoone">Many-to-One</nuxt-link></li>
                    </ul>
                </div>
            </div>
        </nav>
        <nuxt />
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>
