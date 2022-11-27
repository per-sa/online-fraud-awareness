<template>
    <h2 class="mt-5">Latest reports</h2>
    <table class="table table-hover table-bordered mt-5">
        <thead>
            <tr>
                <th scope="col">Time Reported</th>
                <th scope="col">Name</th>
                <th scope="col">Type</th>
                <th scope="col">URL</th>
                <th scope="col">IP Adress</th>
                <th scope="col">Misc.</th>

            </tr>
        </thead>
        <tbody>
            <tr v-for="fraud in latestReports" v-bind:key="fraud.id">
                <th scope="row"> {{ fraud.time_reported }}</th>
                <td>{{ fraud.name }}</td>
                <td>{{ fraud.type }}</td>
                <td><a :href="`${fraud.url}`" target="_blank">{{ fraud.url }}</a> - <a href="">WHOIS</a>
                </td>
                <td>{{ fraud.ip_adress }} - <a href="https://www.arin.net/">ARIN</a></td>
                <td><button class="btn btn-outline-success" type="button">See details</button></td>
            </tr>
        </tbody>
    </table>

</template>

<script>
import axios from "axios";

export default {
    name: "PreviewTable",
    data() {
        return {
            latestReports: [],
        };
    },

    mounted() {
        this.getLatestReports();
    },
    methods: {
        getLatestReports() {
            axios.get("http://127.0.0.1:8000/api/frauds/")
                .then((response) => {
                    this.latestReports = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        }
    },
};
</script>

<style scoped>
thead,
tbody,
th,
td,
tr {
    text-align: center;
    vertical-align: middle;
}
</style>