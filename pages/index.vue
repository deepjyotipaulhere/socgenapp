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
        <div>
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <div class="card border-white shadow">
                            <div class="card-body">
                                <h4 class="card-title">SG Files</h4>
                                <GChart
                                    type="PieChart"
                                    :data="chartData"
                                    :createChart="(el, google) => new google.charts.Pie(el)"
                                    @ready="onChartReady"
                                />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <br>
        <div>
            <div class="container">
                <div class="row">
                    <div class="col-md-4">
                        <div class="card shadow" v-if="matches.length>0">
                            <div class="card-body">
                                <h4 class="card-title">Match Results</h4>
                                <div class="table-responsive">
                                    <table class="table">
                                        <thead>
                                            <tr>
                                                <th>SG Reference</th>
                                                <th>CP Reference</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="(x,i) in matches" :key="i">
                                                <td>{{x[0]}}</td>
                                                <td>{{x[1]}}</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card shadow" v-if="matches.length>0">
                            <div class="card-body">
                                <h4 class="card-title">Mismatch Results</h4>
                                <div class="table-responsive">
                                    <table class="table">
                                        <thead>
                                            <tr>
                                                <th>SG Reference</th>
                                                <!-- <th>CP Reference</th> -->
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="(x,i) in unmatches" :key="i">
                                                <td>{{x[':20']}}</td>
                                                <!-- <td>{{x[1]}}</td> -->
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-4">
                        <div class="card shadow" v-if="matches.length>0">
                            <div class="card-body">
                                <h4 class="card-title">Close Fits</h4>
                                <div class="table-responsive">
                                    <table class="table">
                                        <thead>
                                            <tr>
                                                <th>SG Reference</th>
                                                <!-- <th>CP Reference</th> -->
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr v-for="(x,i) in closefits" :key="i">
                                                <td>{{x}}</td>
                                                <!-- <td>{{x[1]}}</td> -->
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <br><br>
        <div>
            <nav class="navbar navbar-light navbar-expand-md fixed-bottom text-center navigation-clean shadow">
                <div class="container"><button class="navbar-toggler" data-toggle="collapse" data-target="#navcol-1"><span class="sr-only">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
                    <div class="collapse navbar-collapse" id="navcol-1"><button class="btn btn-primary" type="button" @click.prevent="match">Match</button>
                        <ul class="nav navbar-nav ml-auto"></ul>
                    </div>
                </div>
            </nav>
        </div>
    </div>
</template>

<script>
import {GChart} from 'vue-google-charts';
export default {
    data(){
        return {
            files: [],
            cpfiles:[],
            filesuploading:false,
            cpfilesuploading:false,
            getsgfiles:[],
            getcpfiles:[],
            matches:[],
            unmatches:[],
            closefits:[],
            chartData:[],
        }
    },

    components:{
        GChart
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
                    this.$axios.post("/insertsgfiles",formData).then(response=>{
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
                    this.$axios.post("/insertcpfiles",formData).then(response=>{
                    })
                }
            );
            this.cpfilesuploading=false
        },
        match(){
            // this.$axios.get("/getsgfiles").then(response=>{
            //     this.getsgfiles=response.data
            // })
            // this.$axios.get("/getcpfiles").then(response=>{
            //     this.getcpfiles=response.data
            // })
            this.$axios.get("/match").then(response=>{
                this.matches=response.data.match
                this.unmatches=response.data.unmatch
                this.closefits=response.data.closefit
                this.chartData=[
                    ['Status','Count'],
                    ['Match',this.matches.length],
                    ['Mismatch',this.unmatches.length],
                    ['Close Fits',this.closefits.length],
                ]
            }).then(()=>{
                this.drawChart()
            })
        },
        drawChart(){
            // this.$axios.get("http://localhost:5000").then(response=>{
            //     this.chartData=response.data
            // })
        },
        onChartReady (chart, google) {
            this.chartsLib = google
        }
    }
}
</script>

<style>

</style>
