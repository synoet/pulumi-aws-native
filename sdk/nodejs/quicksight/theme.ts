// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Definition of the AWS::QuickSight::Theme Resource Type.
 */
export class Theme extends pulumi.CustomResource {
    /**
     * Get an existing Theme resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Theme {
        return new Theme(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:quicksight:Theme';

    /**
     * Returns true if the given object is an instance of Theme.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Theme {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Theme.__pulumiType;
    }

    /**
     * <p>The Amazon Resource Name (ARN) of the theme.</p>
     */
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly awsAccountId!: pulumi.Output<string>;
    /**
     * <p>The ID of the theme that a custom theme will inherit from. All themes inherit from one of
     * 			the starting themes defined by Amazon QuickSight. For a list of the starting themes, use
     * 				<code>ListThemes</code> or choose <b>Themes</b> from
     * 			within a QuickSight analysis. </p>
     */
    public readonly baseThemeId!: pulumi.Output<string | undefined>;
    public readonly configuration!: pulumi.Output<outputs.quicksight.ThemeThemeConfiguration | undefined>;
    /**
     * <p>The date and time that the theme was created.</p>
     */
    public /*out*/ readonly createdTime!: pulumi.Output<string>;
    /**
     * <p>The date and time that the theme was last updated.</p>
     */
    public /*out*/ readonly lastUpdatedTime!: pulumi.Output<string>;
    /**
     * <p>A display name for the theme.</p>
     */
    public readonly name!: pulumi.Output<string | undefined>;
    /**
     * <p>A valid grouping of resource permissions to apply to the new theme.
     * 			</p>
     */
    public readonly permissions!: pulumi.Output<outputs.quicksight.ThemeResourcePermission[] | undefined>;
    /**
     * <p>A map of the key-value pairs for the resource tag or tags that you want to add to the
     * 			resource.</p>
     */
    public readonly tags!: pulumi.Output<outputs.quicksight.ThemeTag[] | undefined>;
    public readonly themeId!: pulumi.Output<string>;
    public /*out*/ readonly type!: pulumi.Output<enums.quicksight.ThemeThemeType>;
    public /*out*/ readonly version!: pulumi.Output<outputs.quicksight.ThemeThemeVersion>;
    /**
     * <p>A description of the first version of the theme that you're creating. Every time
     * 				<code>UpdateTheme</code> is called, a new version is created. Each version of the
     * 			theme has a description of the version in the <code>VersionDescription</code>
     * 			field.</p>
     */
    public readonly versionDescription!: pulumi.Output<string | undefined>;

    /**
     * Create a Theme resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ThemeArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.awsAccountId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'awsAccountId'");
            }
            if ((!args || args.themeId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'themeId'");
            }
            inputs["awsAccountId"] = args ? args.awsAccountId : undefined;
            inputs["baseThemeId"] = args ? args.baseThemeId : undefined;
            inputs["configuration"] = args ? args.configuration : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["permissions"] = args ? args.permissions : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["themeId"] = args ? args.themeId : undefined;
            inputs["versionDescription"] = args ? args.versionDescription : undefined;
            inputs["arn"] = undefined /*out*/;
            inputs["createdTime"] = undefined /*out*/;
            inputs["lastUpdatedTime"] = undefined /*out*/;
            inputs["type"] = undefined /*out*/;
            inputs["version"] = undefined /*out*/;
        } else {
            inputs["arn"] = undefined /*out*/;
            inputs["awsAccountId"] = undefined /*out*/;
            inputs["baseThemeId"] = undefined /*out*/;
            inputs["configuration"] = undefined /*out*/;
            inputs["createdTime"] = undefined /*out*/;
            inputs["lastUpdatedTime"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["permissions"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["themeId"] = undefined /*out*/;
            inputs["type"] = undefined /*out*/;
            inputs["version"] = undefined /*out*/;
            inputs["versionDescription"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Theme.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Theme resource.
 */
export interface ThemeArgs {
    awsAccountId: pulumi.Input<string>;
    /**
     * <p>The ID of the theme that a custom theme will inherit from. All themes inherit from one of
     * 			the starting themes defined by Amazon QuickSight. For a list of the starting themes, use
     * 				<code>ListThemes</code> or choose <b>Themes</b> from
     * 			within a QuickSight analysis. </p>
     */
    baseThemeId?: pulumi.Input<string>;
    configuration?: pulumi.Input<inputs.quicksight.ThemeThemeConfigurationArgs>;
    /**
     * <p>A display name for the theme.</p>
     */
    name?: pulumi.Input<string>;
    /**
     * <p>A valid grouping of resource permissions to apply to the new theme.
     * 			</p>
     */
    permissions?: pulumi.Input<pulumi.Input<inputs.quicksight.ThemeResourcePermissionArgs>[]>;
    /**
     * <p>A map of the key-value pairs for the resource tag or tags that you want to add to the
     * 			resource.</p>
     */
    tags?: pulumi.Input<pulumi.Input<inputs.quicksight.ThemeTagArgs>[]>;
    themeId: pulumi.Input<string>;
    /**
     * <p>A description of the first version of the theme that you're creating. Every time
     * 				<code>UpdateTheme</code> is called, a new version is created. Each version of the
     * 			theme has a description of the version in the <code>VersionDescription</code>
     * 			field.</p>
     */
    versionDescription?: pulumi.Input<string>;
}
