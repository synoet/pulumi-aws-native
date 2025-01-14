// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::PinpointEmail::Identity
 */
export function getIdentity(args: GetIdentityArgs, opts?: pulumi.InvokeOptions): Promise<GetIdentityResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:pinpointemail:getIdentity", {
        "id": args.id,
    }, opts);
}

export interface GetIdentityArgs {
    id: string;
}

export interface GetIdentityResult {
    readonly dkimSigningEnabled?: boolean;
    readonly feedbackForwardingEnabled?: boolean;
    readonly id?: string;
    readonly identityDnsRecordName1?: string;
    readonly identityDnsRecordName2?: string;
    readonly identityDnsRecordName3?: string;
    readonly identityDnsRecordValue1?: string;
    readonly identityDnsRecordValue2?: string;
    readonly identityDnsRecordValue3?: string;
    readonly mailFromAttributes?: outputs.pinpointemail.IdentityMailFromAttributes;
    readonly tags?: outputs.pinpointemail.IdentityTags[];
}
/**
 * Resource Type definition for AWS::PinpointEmail::Identity
 */
export function getIdentityOutput(args: GetIdentityOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetIdentityResult> {
    return pulumi.output(args).apply((a: any) => getIdentity(a, opts))
}

export interface GetIdentityOutputArgs {
    id: pulumi.Input<string>;
}
