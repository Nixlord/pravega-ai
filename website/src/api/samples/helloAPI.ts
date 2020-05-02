export interface HelloRequest {
    name: string
}
export interface HelloResponse {
    developer: string
}

export default function helloAPI(
    request: HelloRequest
): Promise<HelloResponse> {
    return fetch(`/api/hello/${request.name}`)
        .then(response => response.json())
        .then(json => ({ developer: json.developer }))
}