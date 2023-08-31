// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::Amplify::Domain resource allows you to connect a custom domain to your app.
 */
export class Domain extends pulumi.CustomResource {
    /**
     * Get an existing Domain resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Domain {
        return new Domain(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:amplify:Domain';

    /**
     * Returns true if the given object is an instance of Domain.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Domain {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Domain.__pulumiType;
    }

    public readonly appId!: pulumi.Output<string>;
    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly autoSubDomainCreationPatterns!: pulumi.Output<string[] | undefined>;
    public readonly autoSubDomainIamRole!: pulumi.Output<string | undefined>;
    public /*out*/ readonly certificateRecord!: pulumi.Output<string>;
    public readonly domainName!: pulumi.Output<string>;
    public /*out*/ readonly domainStatus!: pulumi.Output<string>;
    public readonly enableAutoSubDomain!: pulumi.Output<boolean | undefined>;
    public /*out*/ readonly statusReason!: pulumi.Output<string>;
    public readonly subDomainSettings!: pulumi.Output<outputs.amplify.DomainSubDomainSetting[]>;

    /**
     * Create a Domain resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DomainArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.appId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'appId'");
            }
            if ((!args || args.subDomainSettings === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subDomainSettings'");
            }
            resourceInputs["appId"] = args ? args.appId : undefined;
            resourceInputs["autoSubDomainCreationPatterns"] = args ? args.autoSubDomainCreationPatterns : undefined;
            resourceInputs["autoSubDomainIamRole"] = args ? args.autoSubDomainIamRole : undefined;
            resourceInputs["domainName"] = args ? args.domainName : undefined;
            resourceInputs["enableAutoSubDomain"] = args ? args.enableAutoSubDomain : undefined;
            resourceInputs["subDomainSettings"] = args ? args.subDomainSettings : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["certificateRecord"] = undefined /*out*/;
            resourceInputs["domainStatus"] = undefined /*out*/;
            resourceInputs["statusReason"] = undefined /*out*/;
        } else {
            resourceInputs["appId"] = undefined /*out*/;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["autoSubDomainCreationPatterns"] = undefined /*out*/;
            resourceInputs["autoSubDomainIamRole"] = undefined /*out*/;
            resourceInputs["certificateRecord"] = undefined /*out*/;
            resourceInputs["domainName"] = undefined /*out*/;
            resourceInputs["domainStatus"] = undefined /*out*/;
            resourceInputs["enableAutoSubDomain"] = undefined /*out*/;
            resourceInputs["statusReason"] = undefined /*out*/;
            resourceInputs["subDomainSettings"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["appId", "domainName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Domain.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Domain resource.
 */
export interface DomainArgs {
    appId: pulumi.Input<string>;
    autoSubDomainCreationPatterns?: pulumi.Input<pulumi.Input<string>[]>;
    autoSubDomainIamRole?: pulumi.Input<string>;
    domainName?: pulumi.Input<string>;
    enableAutoSubDomain?: pulumi.Input<boolean>;
    subDomainSettings: pulumi.Input<pulumi.Input<inputs.amplify.DomainSubDomainSettingArgs>[]>;
}
