
export interface CriminalRequest {
    
}
export interface CriminalResponse {
    
}

export default function criminalAPI(
    request: CriminalRequest
): Promise<CriminalResponse> {
    return fetch(`/api/neural/facerecognition/criminal`)
        .then(response => response.json())
}


