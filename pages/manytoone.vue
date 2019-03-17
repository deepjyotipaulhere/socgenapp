<template>
    <div>
        <div style="margin-top: 30px;">
            <div class="container">
                <div class="row">
                    <div class="col-md-6" style="background-color: transparent;padding: 1em;">
                        <div class="card bg-white shadow">
                            <div class="card-body">
                                <h4 class="card-title">Upload SG Files</h4>
                                <input type="file" ref="files1" multiple @change="handleFilesUpload1($event.target.files)">
                                <button class="btn btn-primary" type="button" @click.prevent="submitFiles1">Upload</button>
                                </div>
                        </div>
                    </div>
                    <div class="col-md-6" style="background-color: transparent;padding: 1em;">
                        <div class="card bg-white shadow">
                            <div class="card-body">
                                <h4 class="card-title">Upload CP Files</h4>
                                <input type="file" ref="files2" multiple @change="handleFilesUpload2($event.target.files)">
                                <button class="btn btn-primary" type="button" @click.prevent="submitFiles2">Upload</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            files: [],
            cpfiles:[],
            filesuploading:false,
            cpfilesuploading:false,
        }
    },
    methods:{
        handleFilesUpload1(fileList){
            if (!fileList.length) return;
            Array.from(Array(fileList.length).keys())
                .map(x => {
                    this.files[x]=fileList[x];
                }
            );
        },
        handleFilesUpload2(fileList){
            if (!fileList.length) return;
            Array.from(Array(fileList.length).keys())
                .map(x => {
                    this.cpfiles[x]=fileList[x];                                       
                }
            );
        },
        submitFiles1(){
            this.filesuploading=true
            Array.from(Array(this.files.length).keys())
                .map(x => {  
                    const formData = new FormData();
                    formData.append('file',this.files[x]);
                    this.$axios.post("/insertsgfilesmo",formData).then(response=>{
                    })
                }
            );
            this.filesuploading=false
        },
        submitFiles2(){
            this.cpfilesuploading=true
            Array.from(Array(this.cpfiles.length).keys())
                .map(x => {  
                    const formData = new FormData();
                    formData.append('file',this.cpfiles[x]);
                    this.$axios.post("/insertcpfilesmo",formData).then(response=>{
                    })
                }
            );
            this.cpfilesuploading=false
        },
    }
}
</script>

<style>

</style>
