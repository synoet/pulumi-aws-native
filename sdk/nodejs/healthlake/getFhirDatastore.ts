// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * HealthLake FHIR Datastore
 */
export function getFhirDatastore(args: GetFhirDatastoreArgs, opts?: pulumi.InvokeOptions): Promise<GetFhirDatastoreResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:healthlake:getFhirDatastore", {
        "datastoreId": args.datastoreId,
    }, opts);
}

export interface GetFhirDatastoreArgs {
    datastoreId: string;
}

export interface GetFhirDatastoreResult {
    readonly createdAt?: outputs.healthlake.FhirDatastoreCreatedAt;
    readonly datastoreArn?: string;
    readonly datastoreEndpoint?: string;
    readonly datastoreId?: string;
    readonly datastoreStatus?: enums.healthlake.FhirDatastoreDatastoreStatus;
    readonly tags?: outputs.healthlake.FhirDatastoreTag[];
}
/**
 * HealthLake FHIR Datastore
 */
export function getFhirDatastoreOutput(args: GetFhirDatastoreOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetFhirDatastoreResult> {
    return pulumi.output(args).apply((a: any) => getFhirDatastore(a, opts))
}

export interface GetFhirDatastoreOutputArgs {
    datastoreId: pulumi.Input<string>;
}
