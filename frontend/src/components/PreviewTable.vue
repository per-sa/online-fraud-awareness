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
            <tr>
                <th scope="row"> 24/Nov/2022 - 17:41:52</th>
                <td>Jacob</td>
                <td>Phishing</td>
                <td><a href="https://www.google.com" target="_blank">https://www.google.com/</a> - <a href="">WHOIS</a>
                </td>
                <td>198.0.0.1 - <a href="https://www.arin.net/">ARIN</a></td>
                <td><button class="btn btn-outline-success" type="button">See details</button></td>
            </tr>
        </tbody>
    </table>

</template>

<script>
export default {
    name: "PreviewTable",
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