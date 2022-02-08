// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudformation

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "aws-native:cloudformation:CustomResource":
		r = &CustomResource{}
	case "aws-native:cloudformation:HookDefaultVersion":
		r = &HookDefaultVersion{}
	case "aws-native:cloudformation:HookTypeConfig":
		r = &HookTypeConfig{}
	case "aws-native:cloudformation:HookVersion":
		r = &HookVersion{}
	case "aws-native:cloudformation:Macro":
		r = &Macro{}
	case "aws-native:cloudformation:ModuleDefaultVersion":
		r = &ModuleDefaultVersion{}
	case "aws-native:cloudformation:ModuleVersion":
		r = &ModuleVersion{}
	case "aws-native:cloudformation:PublicTypeVersion":
		r = &PublicTypeVersion{}
	case "aws-native:cloudformation:Publisher":
		r = &Publisher{}
	case "aws-native:cloudformation:ResourceDefaultVersion":
		r = &ResourceDefaultVersion{}
	case "aws-native:cloudformation:ResourceVersion":
		r = &ResourceVersion{}
	case "aws-native:cloudformation:Stack":
		r = &Stack{}
	case "aws-native:cloudformation:StackSet":
		r = &StackSet{}
	case "aws-native:cloudformation:TypeActivation":
		r = &TypeActivation{}
	case "aws-native:cloudformation:WaitCondition":
		r = &WaitCondition{}
	case "aws-native:cloudformation:WaitConditionHandle":
		r = &WaitConditionHandle{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

func init() {
	version, err := aws.PkgVersion()
	if err != nil {
		fmt.Printf("failed to determine package version. defaulting to v1: %v\n", err)
	}
	pulumi.RegisterResourceModule(
		"aws-native",
		"cloudformation",
		&module{version},
	)
}
