// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Config::OrganizationConfigRule
 *
 * @deprecated OrganizationConfigRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class OrganizationConfigRule extends pulumi.CustomResource {
    /**
     * Get an existing OrganizationConfigRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): OrganizationConfigRule {
        pulumi.log.warn("OrganizationConfigRule is deprecated: OrganizationConfigRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new OrganizationConfigRule(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:configuration:OrganizationConfigRule';

    /**
     * Returns true if the given object is an instance of OrganizationConfigRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is OrganizationConfigRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === OrganizationConfigRule.__pulumiType;
    }

    public readonly excludedAccounts!: pulumi.Output<string[] | undefined>;
    public readonly organizationConfigRuleName!: pulumi.Output<string>;
    public readonly organizationCustomPolicyRuleMetadata!: pulumi.Output<outputs.configuration.OrganizationConfigRuleOrganizationCustomPolicyRuleMetadata | undefined>;
    public readonly organizationCustomRuleMetadata!: pulumi.Output<outputs.configuration.OrganizationConfigRuleOrganizationCustomRuleMetadata | undefined>;
    public readonly organizationManagedRuleMetadata!: pulumi.Output<outputs.configuration.OrganizationConfigRuleOrganizationManagedRuleMetadata | undefined>;

    /**
     * Create a OrganizationConfigRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated OrganizationConfigRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args?: OrganizationConfigRuleArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("OrganizationConfigRule is deprecated: OrganizationConfigRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["excludedAccounts"] = args ? args.excludedAccounts : undefined;
            resourceInputs["organizationConfigRuleName"] = args ? args.organizationConfigRuleName : undefined;
            resourceInputs["organizationCustomPolicyRuleMetadata"] = args ? args.organizationCustomPolicyRuleMetadata : undefined;
            resourceInputs["organizationCustomRuleMetadata"] = args ? args.organizationCustomRuleMetadata : undefined;
            resourceInputs["organizationManagedRuleMetadata"] = args ? args.organizationManagedRuleMetadata : undefined;
        } else {
            resourceInputs["excludedAccounts"] = undefined /*out*/;
            resourceInputs["organizationConfigRuleName"] = undefined /*out*/;
            resourceInputs["organizationCustomPolicyRuleMetadata"] = undefined /*out*/;
            resourceInputs["organizationCustomRuleMetadata"] = undefined /*out*/;
            resourceInputs["organizationManagedRuleMetadata"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["organizationConfigRuleName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(OrganizationConfigRule.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a OrganizationConfigRule resource.
 */
export interface OrganizationConfigRuleArgs {
    excludedAccounts?: pulumi.Input<pulumi.Input<string>[]>;
    organizationConfigRuleName?: pulumi.Input<string>;
    organizationCustomPolicyRuleMetadata?: pulumi.Input<inputs.configuration.OrganizationConfigRuleOrganizationCustomPolicyRuleMetadataArgs>;
    organizationCustomRuleMetadata?: pulumi.Input<inputs.configuration.OrganizationConfigRuleOrganizationCustomRuleMetadataArgs>;
    organizationManagedRuleMetadata?: pulumi.Input<inputs.configuration.OrganizationConfigRuleOrganizationManagedRuleMetadataArgs>;
}
