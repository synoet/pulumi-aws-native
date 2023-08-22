// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::InstanceConnectEndpoint
 */
export function getInstanceConnectEndpoint(args: GetInstanceConnectEndpointArgs, opts?: pulumi.InvokeOptions): Promise<GetInstanceConnectEndpointResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ec2:getInstanceConnectEndpoint", {
        "id": args.id,
    }, opts);
}

export interface GetInstanceConnectEndpointArgs {
    /**
     * The id of the instance connect endpoint
     */
    id: string;
}

export interface GetInstanceConnectEndpointResult {
    /**
     * The id of the instance connect endpoint
     */
    readonly id?: string;
    /**
     * The tags of the instance connect endpoint.
     */
    readonly tags?: outputs.ec2.InstanceConnectEndpointTag[];
}
/**
 * Resource Type definition for AWS::EC2::InstanceConnectEndpoint
 */
export function getInstanceConnectEndpointOutput(args: GetInstanceConnectEndpointOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetInstanceConnectEndpointResult> {
    return pulumi.output(args).apply((a: any) => getInstanceConnectEndpoint(a, opts))
}

export interface GetInstanceConnectEndpointOutputArgs {
    /**
     * The id of the instance connect endpoint
     */
    id: pulumi.Input<string>;
}
