// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::WAF::IPSet
 */
export function getIpSet(args: GetIpSetArgs, opts?: pulumi.InvokeOptions): Promise<GetIpSetResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:waf:getIpSet", {
        "id": args.id,
    }, opts);
}

export interface GetIpSetArgs {
    id: string;
}

export interface GetIpSetResult {
    readonly id?: string;
    readonly ipSetDescriptors?: outputs.waf.IpSetIpSetDescriptor[];
}
/**
 * Resource Type definition for AWS::WAF::IPSet
 */
export function getIpSetOutput(args: GetIpSetOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetIpSetResult> {
    return pulumi.output(args).apply((a: any) => getIpSet(a, opts))
}

export interface GetIpSetOutputArgs {
    id: pulumi.Input<string>;
}
