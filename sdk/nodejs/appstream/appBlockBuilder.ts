// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AppStream::AppBlockBuilder.
 */
export class AppBlockBuilder extends pulumi.CustomResource {
    /**
     * Get an existing AppBlockBuilder resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): AppBlockBuilder {
        return new AppBlockBuilder(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:appstream:AppBlockBuilder';

    /**
     * Returns true if the given object is an instance of AppBlockBuilder.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AppBlockBuilder {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AppBlockBuilder.__pulumiType;
    }

    public readonly accessEndpoints!: pulumi.Output<outputs.appstream.AppBlockBuilderAccessEndpoint[] | undefined>;
    public readonly appBlockArns!: pulumi.Output<string[] | undefined>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public /*out*/ readonly createdTime!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly displayName!: pulumi.Output<string | undefined>;
    public readonly enableDefaultInternetAccess!: pulumi.Output<boolean | undefined>;
    public readonly iamRoleArn!: pulumi.Output<string | undefined>;
    public readonly instanceType!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<string>;
    public readonly platform!: pulumi.Output<string>;
    public readonly tags!: pulumi.Output<outputs.appstream.AppBlockBuilderTag[] | undefined>;
    public readonly vpcConfig!: pulumi.Output<outputs.appstream.AppBlockBuilderVpcConfig>;

    /**
     * Create a AppBlockBuilder resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AppBlockBuilderArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.instanceType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceType'");
            }
            if ((!args || args.platform === undefined) && !opts.urn) {
                throw new Error("Missing required property 'platform'");
            }
            if ((!args || args.vpcConfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'vpcConfig'");
            }
            resourceInputs["accessEndpoints"] = args ? args.accessEndpoints : undefined;
            resourceInputs["appBlockArns"] = args ? args.appBlockArns : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["displayName"] = args ? args.displayName : undefined;
            resourceInputs["enableDefaultInternetAccess"] = args ? args.enableDefaultInternetAccess : undefined;
            resourceInputs["iamRoleArn"] = args ? args.iamRoleArn : undefined;
            resourceInputs["instanceType"] = args ? args.instanceType : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["platform"] = args ? args.platform : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["vpcConfig"] = args ? args.vpcConfig : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["createdTime"] = undefined /*out*/;
        } else {
            resourceInputs["accessEndpoints"] = undefined /*out*/;
            resourceInputs["appBlockArns"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["createdTime"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["displayName"] = undefined /*out*/;
            resourceInputs["enableDefaultInternetAccess"] = undefined /*out*/;
            resourceInputs["iamRoleArn"] = undefined /*out*/;
            resourceInputs["instanceType"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["platform"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["vpcConfig"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["name"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(AppBlockBuilder.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a AppBlockBuilder resource.
 */
export interface AppBlockBuilderArgs {
    accessEndpoints?: pulumi.Input<pulumi.Input<inputs.appstream.AppBlockBuilderAccessEndpointArgs>[]>;
    appBlockArns?: pulumi.Input<pulumi.Input<string>[]>;
    description?: pulumi.Input<string>;
    displayName?: pulumi.Input<string>;
    enableDefaultInternetAccess?: pulumi.Input<boolean>;
    iamRoleArn?: pulumi.Input<string>;
    instanceType: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    platform: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.appstream.AppBlockBuilderTagArgs>[]>;
    vpcConfig: pulumi.Input<inputs.appstream.AppBlockBuilderVpcConfigArgs>;
}
