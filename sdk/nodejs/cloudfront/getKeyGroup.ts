// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CloudFront::KeyGroup
 */
export function getKeyGroup(args: GetKeyGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetKeyGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:cloudfront:getKeyGroup", {
        "id": args.id,
    }, opts);
}

export interface GetKeyGroupArgs {
    id: string;
}

export interface GetKeyGroupResult {
    readonly id?: string;
    readonly keyGroupConfig?: outputs.cloudfront.KeyGroupConfig;
    readonly lastModifiedTime?: string;
}
/**
 * Resource Type definition for AWS::CloudFront::KeyGroup
 */
export function getKeyGroupOutput(args: GetKeyGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetKeyGroupResult> {
    return pulumi.output(args).apply((a: any) => getKeyGroup(a, opts))
}

export interface GetKeyGroupOutputArgs {
    id: pulumi.Input<string>;
}
