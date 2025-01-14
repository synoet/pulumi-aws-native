// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Connect::View
 */
export function getView(args: GetViewArgs, opts?: pulumi.InvokeOptions): Promise<GetViewResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:connect:getView", {
        "viewArn": args.viewArn,
    }, opts);
}

export interface GetViewArgs {
    /**
     * The Amazon Resource Name (ARN) of the view.
     */
    viewArn: string;
}

export interface GetViewResult {
    /**
     * The actions of the view in an array.
     */
    readonly actions?: string[];
    /**
     * The description of the view.
     */
    readonly description?: string;
    /**
     * The Amazon Resource Name (ARN) of the instance.
     */
    readonly instanceArn?: string;
    /**
     * The name of the view.
     */
    readonly name?: string;
    /**
     * One or more tags.
     */
    readonly tags?: outputs.connect.ViewTag[];
    /**
     * The template of the view as JSON.
     */
    readonly template?: any;
    /**
     * The Amazon Resource Name (ARN) of the view.
     */
    readonly viewArn?: string;
    /**
     * The view content hash.
     */
    readonly viewContentSha256?: string;
    /**
     * The view id of the view.
     */
    readonly viewId?: string;
}
/**
 * Resource Type definition for AWS::Connect::View
 */
export function getViewOutput(args: GetViewOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetViewResult> {
    return pulumi.output(args).apply((a: any) => getView(a, opts))
}

export interface GetViewOutputArgs {
    /**
     * The Amazon Resource Name (ARN) of the view.
     */
    viewArn: pulumi.Input<string>;
}
