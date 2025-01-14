// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Pinpoint::APNSVoipChannel
 */
export function getApnsVoipChannel(args: GetApnsVoipChannelArgs, opts?: pulumi.InvokeOptions): Promise<GetApnsVoipChannelResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:pinpoint:getApnsVoipChannel", {
        "id": args.id,
    }, opts);
}

export interface GetApnsVoipChannelArgs {
    id: string;
}

export interface GetApnsVoipChannelResult {
    readonly bundleId?: string;
    readonly certificate?: string;
    readonly defaultAuthenticationMethod?: string;
    readonly enabled?: boolean;
    readonly id?: string;
    readonly privateKey?: string;
    readonly teamId?: string;
    readonly tokenKey?: string;
    readonly tokenKeyId?: string;
}
/**
 * Resource Type definition for AWS::Pinpoint::APNSVoipChannel
 */
export function getApnsVoipChannelOutput(args: GetApnsVoipChannelOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetApnsVoipChannelResult> {
    return pulumi.output(args).apply((a: any) => getApnsVoipChannel(a, opts))
}

export interface GetApnsVoipChannelOutputArgs {
    id: pulumi.Input<string>;
}
