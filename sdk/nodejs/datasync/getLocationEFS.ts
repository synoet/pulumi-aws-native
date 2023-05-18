// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::DataSync::LocationEFS.
 */
export function getLocationEFS(args: GetLocationEFSArgs, opts?: pulumi.InvokeOptions): Promise<GetLocationEFSResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:datasync:getLocationEFS", {
        "locationArn": args.locationArn,
    }, opts);
}

export interface GetLocationEFSArgs {
    /**
     * The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
     */
    locationArn: string;
}

export interface GetLocationEFSResult {
    /**
     * The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
     */
    readonly locationArn?: string;
    /**
     * The URL of the EFS location that was described.
     */
    readonly locationUri?: string;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.datasync.LocationEFSTag[];
}
/**
 * Resource schema for AWS::DataSync::LocationEFS.
 */
export function getLocationEFSOutput(args: GetLocationEFSOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLocationEFSResult> {
    return pulumi.output(args).apply((a: any) => getLocationEFS(a, opts))
}

export interface GetLocationEFSOutputArgs {
    /**
     * The Amazon Resource Name (ARN) of the Amazon EFS file system location that is created.
     */
    locationArn: pulumi.Input<string>;
}
