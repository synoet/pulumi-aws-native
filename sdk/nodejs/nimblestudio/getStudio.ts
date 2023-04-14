// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Represents a studio that contains other Nimble Studio resources
 */
export function getStudio(args: GetStudioArgs, opts?: pulumi.InvokeOptions): Promise<GetStudioResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:nimblestudio:getStudio", {
        "studioId": args.studioId,
    }, opts);
}

export interface GetStudioArgs {
    studioId: string;
}

export interface GetStudioResult {
    /**
     * <p>The IAM role that Studio Admins will assume when logging in to the Nimble Studio portal.</p>
     */
    readonly adminRoleArn?: string;
    /**
     * <p>A friendly name for the studio.</p>
     */
    readonly displayName?: string;
    /**
     * <p>The Amazon Web Services Region where the studio resource is located.</p>
     */
    readonly homeRegion?: string;
    /**
     * <p>The Amazon Web Services SSO application client ID used to integrate with Amazon Web Services SSO to enable Amazon Web Services SSO users to log in to Nimble Studio portal.</p>
     */
    readonly ssoClientId?: string;
    readonly studioEncryptionConfiguration?: outputs.nimblestudio.StudioEncryptionConfiguration;
    readonly studioId?: string;
    /**
     * <p>The address of the web page for the studio.</p>
     */
    readonly studioUrl?: string;
    /**
     * <p>The IAM role that Studio Users will assume when logging in to the Nimble Studio portal.</p>
     */
    readonly userRoleArn?: string;
}
/**
 * Represents a studio that contains other Nimble Studio resources
 */
export function getStudioOutput(args: GetStudioOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetStudioResult> {
    return pulumi.output(args).apply((a: any) => getStudio(a, opts))
}

export interface GetStudioOutputArgs {
    studioId: pulumi.Input<string>;
}
