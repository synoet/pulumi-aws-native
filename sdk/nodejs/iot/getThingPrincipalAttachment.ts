// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::IoT::ThingPrincipalAttachment
 */
export function getThingPrincipalAttachment(args: GetThingPrincipalAttachmentArgs, opts?: pulumi.InvokeOptions): Promise<GetThingPrincipalAttachmentResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:iot:getThingPrincipalAttachment", {
        "id": args.id,
    }, opts);
}

export interface GetThingPrincipalAttachmentArgs {
    id: string;
}

export interface GetThingPrincipalAttachmentResult {
    readonly id?: string;
}
/**
 * Resource Type definition for AWS::IoT::ThingPrincipalAttachment
 */
export function getThingPrincipalAttachmentOutput(args: GetThingPrincipalAttachmentOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetThingPrincipalAttachmentResult> {
    return pulumi.output(args).apply((a: any) => getThingPrincipalAttachment(a, opts))
}

export interface GetThingPrincipalAttachmentOutputArgs {
    id: pulumi.Input<string>;
}
